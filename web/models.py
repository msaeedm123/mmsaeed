from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)