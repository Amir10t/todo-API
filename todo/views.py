from django.shortcuts import render
from rest_framework import generics
from todo.models import TodoModel, User
from todo.serializer import TodoSerializer, UserSerializer


# Create your views here.
#region TODOS APIVIEW
class TodoListAPIView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.order_by('priority').all()
    serializer_class = TodoSerializer

class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.order_by('priority').all()
    serializer_class = TodoSerializer
#endregion

#region USER APIVIEW
class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#endregion