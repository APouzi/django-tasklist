from django.http import request
from django.shortcuts import render
# from backend.taskList.models import Task
from .serializers import UserSerializerWithToken, UserSerializer, TaskSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
# from models import Tasks

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView

# Models
from .models import Task

from rest_framework import permissions

# Class Based: 
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer): 
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# Create your views here.


@api_view(['POST'])
def registerUser(request):
    try:
        data = request.data
        user = User.objects.create(
            username = data['email'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many = False)
        return Response(serializer.data)
    except:
        message = {'details':'User with this email already exists'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)

# class SnippetList(APIView):
#     def post(self, request, format=None):
#         try:
#             data = request.data
#             user = User.objects.create(
#                 username = data['email'],
#                 email = data['email'],
#                 password = make_password(data['password'])
#             )
#             serializer = UserSerializerWithToken(user, many = False)
#             return Response(serializer.data)
#         except:
#             message = {'details':'User with this email already exists'}
#             return Response(message, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getTaskList(request):
#     user = request.user
#     tasks = user.task_set.all()
#     serializer = TaskSerializer(tasks, many = True)
#     return Response(serializer.data)
    
# class GetTaskList(APIView):
#     def get(self, request, format =None):
#         user = request.user
#         tasks = user.task_set.all()
#         serializer = TaskSerializer(tasks, many = True)
#         return Response(serializer.data)

class GetTaskList(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        user = self.request.user
        return user.task_set.all()
    
    

class CreateTask(CreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class UpdateTask(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_object(self):
        pullOutData = self.request.data
        data = Task.objects.filter(user = self.request.user).get(title = pullOutData['titleToChange'])
        return data


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTask(request):
    user = request.user
    data = request.data
    product = Task.objects.create(
        user = user,
        title = data['title'],
        body = ['title'],
    )

    serializer = TaskSerializer(product, many = False)
    return Response(serializer.data)

        


