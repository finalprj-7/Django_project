from django.db import models
from django.contrib.auth.models import User


class ChatMessage(models.Model):
    room_name = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # User 모델과의 연결
#    style = models.TextField(default="")

    def __str__(self):
        return f'{self.user.username}: {self.message}'