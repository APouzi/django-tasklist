from dataclasses import fields
from .models import Task
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserTaskList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username']
    
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','email','username', 'token', 'password']
        extra_kwargs = {'password':{"write_only":True}}
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    def create(self, validated_data):
        password = validated_data.pop('password')
        createdUser = self.Meta.model.objects.create_user(**validated_data)
        createdUser.set_password(password)
        UserTaskList.objects.create(
            user = createdUser,
            username = validated_data.pop('username')
        )
        return createdUser

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','body', 'listof']

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTaskList
        fields = ["user","username"]