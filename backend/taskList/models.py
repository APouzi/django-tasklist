from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null = True, blank=True)
    body = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title
# Create your models here.

