from django.contrib.auth.models import User
from django.db import models

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Kullanıcı boş olabilir
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation with {self.user.username if self.user else 'Unknown'} - {self.title}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)  # Konuşma ile ilişkilendirme
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # Mesajı gönderen kullanıcı
    message = models.TextField()  # Mesaj metni
    created_at = models.DateTimeField(auto_now_add=True)  # Mesaj zamanı

    def __str__(self):
        return f"Message from {self.sender.username} at {self.created_at}"
