from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, StreamingHttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Conversation, Message, PsychologicalSurvey
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import json


# Anasayfa view'i
def home(request):
    # Kullanıcı giriş yapmışsa, anket durumunu kontrol et
    if request.user.is_authenticated:
        has_survey = PsychologicalSurvey.objects.filter(user=request.user).exists()
        return render(request, 'ui/home.html', {'has_survey': has_survey})
    return render(request, 'ui/home.html')

# Chatbot view'i
@login_required
def chatbot(request):
    conversations = Conversation.objects.filter(user=request.user).order_by('-created_at')  # Kullanıcının konuşmalarını en yeniden eskiye sırala
    return render(request, 'ui/chatbot.html', {'conversations': conversations})

# Kayıt view'i
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'ui/register.html', {'form': form})

# Konuşma silme view'i
@csrf_exempt
@login_required
def delete_conversation(request, conversation_id):
    if request.method == "POST":
        try:
            conversation = Conversation.objects.get(id=conversation_id, user=request.user)
            # Konuşma silindiğinde ilgili memory'yi de sil
            memory_key = f"chat_messages_{conversation_id}"
            if memory_key in request.session:
                del request.session[memory_key]
                request.session.modified = True
            conversation.delete()
            return JsonResponse({"status": "success"})
        except Conversation.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Conversation not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Conversation

def get_conversation_messages(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)

    # Mesajları al
    messages = conversation.messages.all().order_by('created_at')

    # Mesajları JSON formatında döndür
    messages_data = []
    for message in messages:
        messages_data.append({
            'sender': message.sender.username,
            'message': message.message,
            'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Mesajın tarihini formatlayarak ekleyelim
        })

    return JsonResponse({'messages': messages_data})

# Chatbot view'i
@login_required
def newchatbot(request):
    conversations = Conversation.objects.all()  # Tüm konuşmaları çek
    return render(request, 'ui/newchatbot.html', {'conversations': conversations})


import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from langchain.memory import ConversationBufferMemory
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# API ve Model Ayarları
API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "therapyz-llama-3-8b"

# Django Session ile LangChain Memory Yönetimi
def get_memory(session, conversation_id=None):
    # Her sohbet için benzersiz bir session key oluştur
    memory_key = f"chat_messages_{conversation_id}" if conversation_id else "chat_messages_new"
    
    memory = ConversationBufferMemory(return_messages=True)
    
    # Session'dan mesajları al veya yeni başlat
    if memory_key not in session:
        session[memory_key] = []
        # Sistem mesajını ekle
        memory.chat_memory.add_message(
            SystemMessage(content="Sen, terapi yapabilen profesyonel bir psikologsun; kullanıcının duygularını anlamak, farkındalık kazanmasına yardımcı olmak ve bilimsel terapi teknikleriyle rehberlik etmek için buradasın. Kullanıcının paylaştığı durumu empatik bir yaklaşımla dinleyerek açık uçlu ve kısa sorular sor ve yanıt bekle, yanıtları dikkatlice oku ve sohbete devam et. Onun kendini yargılamadan ifade etmesini teşvik et, düşünme biçimlerini keşfetmesine yardımcı ol ve gerektiğinde günlük hayata uygulanabilir öneriler ver. Amacın, kullanıcıya kendi çözümünü bulmasında rehberlik etmek.")
        )
    else:
        # Session'daki mesajları LangChain memory'ye yükle
        for msg in session[memory_key]:
            if msg["role"] == "user":
                memory.chat_memory.add_message(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                memory.chat_memory.add_message(AIMessage(content=msg["content"]))
            elif msg["role"] == "system":
                memory.chat_memory.add_message(SystemMessage(content=msg["content"]))
    
    return memory, memory_key

def save_to_session(session, memory, memory_key):
    # Memory'deki mesajları session'a kaydet
    messages = []
    for msg in memory.chat_memory.messages:
        if isinstance(msg, HumanMessage):
            role = "user"
        elif isinstance(msg, AIMessage):
            role = "assistant"
        elif isinstance(msg, SystemMessage):
            role = "system"
        else:
            continue
            
        messages.append({
            "role": role,
            "content": msg.content
        })
    
    session[memory_key] = messages
    session.modified = True

@csrf_exempt
def chatbot_reply(request):
    if request.method == 'POST':
        try:
            user_message = request.POST.get('message')
            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)

            session = request.session
            user = request.user

            # Aktif konuşmayı al veya yeni oluştur
            conversation = None
            conversation_id = request.POST.get('conversation_id')
            
            if conversation_id:
                try:
                    conversation = Conversation.objects.get(id=conversation_id)
                except Conversation.DoesNotExist:
                    pass
            
            if not conversation:
                conversation = Conversation.objects.create(
                    user=user if user.is_authenticated else None,
                    title=user_message[:50] + "..."
                )

            # Kullanıcı mesajını veritabanına kaydet
            Message.objects.create(
                conversation=conversation,
                sender=user if user.is_authenticated else User.objects.get(username='ChatBot'),
                message=user_message
            )

            # LangChain memory'yi al ve kullanıcı mesajını ekle
            memory, memory_key = get_memory(session, conversation.id)
            memory.chat_memory.add_message(HumanMessage(content=user_message))

            # API'ye gönderilecek veriyi hazırla
            chat_history = memory.chat_memory.messages
            formatted_messages = [
                {"role": "user" if isinstance(msg, HumanMessage) else "assistant" if isinstance(msg, AIMessage) else "system", 
                 "content": msg.content} 
                for msg in chat_history
            ]

            payload = {
                "model": MODEL_NAME,
                "messages": formatted_messages,
                "temperature": 0.3,
                "max_tokens": 256,
                "stream": True,  # Stream'i aktif hale getir
            }

            def generate_stream():
                try:
                    response = requests.post(API_URL, json=payload, stream=True)
                    response.raise_for_status()
                    
                    complete_response = ""
                    
                    for line in response.iter_lines():
                        if line:
                            line = line.decode('utf-8')
                            if line.startswith('data: '):
                                try:
                                    json_str = line[6:]  # 'data: ' prefix'ini kaldır
                                    if json_str.strip() == '[DONE]':
                                        break
                                    
                                    json_data = json.loads(json_str)
                                    if 'choices' in json_data and len(json_data['choices']) > 0:
                                        delta = json_data['choices'][0].get('delta', {})
                                        if 'content' in delta:
                                            content = delta['content']
                                            complete_response += content
                                            yield f"data: {json.dumps({'content': content, 'type': 'token'})}\n\n"
                                except json.JSONDecodeError:
                                    continue

                    # Tüm yanıt tamamlandığında, veritabanına kaydet
                    if complete_response:
                        Message.objects.create(
                            conversation=conversation,
                            sender=User.objects.get(username='ChatBot'),
                            message=complete_response
                        )
                        
                        # Memory'yi güncelle
                        memory.chat_memory.add_message(AIMessage(content=complete_response))
                        save_to_session(session, memory, memory_key)
                        
                        # Final mesajını gönder
                        yield f"data: {json.dumps({'content': complete_response, 'type': 'complete', 'conversation_id': conversation.id})}\n\n"
                
                except Exception as e:
                    yield f"data: {json.dumps({'error': str(e)})}\n\n"

            return StreamingHttpResponse(
                generate_stream(),
                content_type='text/event-stream'
            )
                
        except Exception as e:
            return JsonResponse({
                'error': f'Server error: {str(e)}'
            }, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
@csrf_exempt
def save_survey(request):
    if request.method == 'POST':
        try:
            # Anket verilerini al
            survey = PsychologicalSurvey.objects.create(
                user=request.user,
                stress_level=int(request.POST.get('stress')),
                anxiety_level=int(request.POST.get('anxiety')),
                depression_level=int(request.POST.get('depression')),
                sleep_quality=int(request.POST.get('sleep')),
                life_satisfaction=int(request.POST.get('satisfaction'))
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
def profile(request):
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            # Profil güncelleme
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            messages.success(request, 'Profil bilgileriniz başarıyla güncellendi.')
            
        elif 'change_password' in request.POST:
            # Şifre değiştirme
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Şifreniz başarıyla güncellendi!')
            else:
                messages.error(request, 'Lütfen hataları düzeltin.')
                return render(request, 'ui/profile.html', {
                    'password_form': form,
                    'active_tab': 'password'
                })
                
    password_form = PasswordChangeForm(request.user)
    return render(request, 'ui/profile.html', {
        'password_form': password_form,
        'active_tab': request.POST.get('active_tab', 'profile')
    })
