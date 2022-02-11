from .models import Task
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username']
    
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','email','username', 'token']
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['user','title','body']
