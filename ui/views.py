from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Conversation, Message, PsychologicalSurvey
from django.contrib.auth.models import User


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
API_URL = "http://10.95.48.119:1234/v1/chat/completions"
MODEL_NAME = "turkish-llama-8b-instruct-v0.1"

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
            SystemMessage(content="Sen uzman bir psikologsun. Türkçe konuşuyorsun. Terapi yapıyorsun. Adım adım sohbeti ilerlet ve öneri ver.")
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
                # Yeni konuşma oluşturulduğunda, yeni bir memory başlat
                conversation = Conversation.objects.create(
                    user=user if user.is_authenticated else None,
                    title=user_message[:50] + "..."  # İlk mesajı başlık olarak kullan
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
                "temperature": 0.7,
                "max_tokens": -1,
                "stream": False
            }

            try:
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()  # HTTP hatalarını yakala
                
                bot_reply = response.json()["choices"][0]["message"]["content"]
                
                # Bot yanıtını LangChain memory'ye ekle
                memory.chat_memory.add_message(AIMessage(content=bot_reply))
                
                # Memory'yi session'a kaydet
                save_to_session(session, memory, memory_key)
                
                # Bot mesajını veritabanına kaydet
                Message.objects.create(
                    conversation=conversation,
                    sender=User.objects.get(username='ChatBot'),
                    message=bot_reply
                )

                return JsonResponse({
                    'bot_reply': bot_reply,
                    'conversation_id': conversation.id
                })
                
            except requests.RequestException as e:
                return JsonResponse({
                    'error': f'API request failed: {str(e)}'
                }, status=500)
                
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
