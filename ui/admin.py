from django.contrib import admin
from .models import Conversation, Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')  # Admin panelinde gösterilecek sütunlar
    search_fields = ('user__username', 'title')  # Kullanıcı adı ve başlığa göre arama yapma
    list_filter = ('created_at',)  # Tarihe göre filtreleme
    ordering = ('-created_at',)  # En yeni konuşmalar önce listelensin

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'sender', 'message', 'created_at')  # Admin panelinde gösterilecek sütunlar
    search_fields = ('sender__username', 'message')  # Mesaj içeriğine ve gönderene göre arama yapma
    list_filter = ('created_at', 'sender')  # Tarih ve gönderen kişiye göre filtreleme
    ordering = ('-created_at',)  # En yeni mesajlar önce listelensin

