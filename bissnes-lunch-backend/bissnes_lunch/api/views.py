from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 


# Create your views here.
from documents.models import Documents
from documents.serializers import DocumentSerializer

from todo.models import Todo
from todo.serializers import TodoSerializer


class DocumentModelViewSet(ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer

class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
