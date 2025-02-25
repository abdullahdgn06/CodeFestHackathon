from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('conversation/<int:conversation_id>/messages/', views.get_conversation_messages, name='get_conversation_messages'),
    path('chatbot-reply/', views.chatbot_reply, name='chatbot_reply'),
    path('chatbot/', views.chatbot, name='chatbot'),  # Chatbot view'i için URL yönlendirmesi
    path('newchatbot/', views.newchatbot, name='newchatbot'),  # Chatbot view'i için URL yönlendirmesi
    path('', views.home, name='home'),  # Anasayfa
    path('login/', auth_views.LoginView.as_view(template_name='ui/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django'nun kendi logout view'ı
    path('delete_conversation/<int:conversation_id>/', views.delete_conversation, name='delete_conversation'),
    path('register/', views.register, name='register'),
]

