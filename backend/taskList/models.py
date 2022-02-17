from django.db import models
from django.contrib.auth.models import User


class UserTaskList(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null = False)
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username



class Task(models.Model):
    
    title = models.CharField(max_length=200, null = True, blank=True)
    body = models.TextField(null=True, blank=True)
    listof = models.ForeignKey(UserTaskList, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return self.title
# Create your models here.

