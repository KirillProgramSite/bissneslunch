from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    surname = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50, default='Стажер')
