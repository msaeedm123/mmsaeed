from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return "{} token".format(self.user)


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.date,self.amount)


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.date,self.amount)
