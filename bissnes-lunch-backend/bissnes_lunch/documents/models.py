from django.db import models
from users.models import User

# Create your models here.
class Documents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_weekend = models.CharField(max_length=300)
    date_from = models.CharField(max_length=100)
    days_weekend = models.IntegerField(default=1)
    date = models.DateField(editable=True,)


    def __str__(self):
        return f'{self.user} - {self.type_weekend}'