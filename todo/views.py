from django.shortcuts import render
from rest_framework import generics
from todo.models import TodoModel
from todo.serializer import TodoSerializer


# Create your views here.

class TodoListAPIView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.order_by('priority').all()
    serializer_class = TodoSerializer

class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.order_by('priority').all()
    serializer_class = TodoSerializer