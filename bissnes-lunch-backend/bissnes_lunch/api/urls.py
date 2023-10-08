from django.contrib import admin
from django.urls import path, include

from api.views import DocumentModelViewSet, TodoModelViewSet

from rest_framework import routers



app_name = 'api'

router = routers.DefaultRouter()
router.register(r'documents', DocumentModelViewSet)
router.register(r'todo', TodoModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
