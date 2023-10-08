from django.contrib import admin
from django.urls import path

from api.views import DocumentAPIView

app_name = 'api'

urlpatterns = [
    path('documents-list', DocumentAPIView.as_view()),
]
