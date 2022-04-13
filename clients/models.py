from django.db import models

from user_db.models import User
# Create your models here.

class Client(models.Model):
    channel_name = models.CharField(max_length = 200)
    pid = models.UUIDField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)