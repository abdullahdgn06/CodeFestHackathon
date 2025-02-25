from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Conversation, Message

# Chatbot cevabı
@csrf_exempt
def chatbot_reply(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        user_name = request.POST.get('user_name')

        # Yeni bir konuşma oluşturma
        conversation = Conversation.objects.create(user_name=user_name, title='Yeni Konuşma')

        # Kullanıcı mesajını kaydetme
        Message.objects.create(conversation=conversation, sender='User', message=user_message)

        # Bot yanıtı
        bot_reply = "Bu bir test cevabıdır."

        # Bot cevabını kaydetme
        Message.objects.create(conversation=conversation, sender='Bot', message=bot_reply)

        return JsonResponse({'bot_reply': bot_reply})

    return JsonResponse({'error': 'Invalid request'}, status=400)

# Anasayfa view'i
def home(request):
    return render(request, 'ui/home.html')

# Chatbot view'i
@login_required
def chatbot(request):
    conversations = Conversation.objects.all()  # Tüm konuşmaları çek
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
