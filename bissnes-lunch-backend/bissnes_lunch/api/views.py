from django.shortcuts import render
from rest_framework.generics import ListAPIView


# Create your views here.
from documents.models import Documents
from documents.serializers import DocumentSerializer


class DocumentAPIView(ListAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
