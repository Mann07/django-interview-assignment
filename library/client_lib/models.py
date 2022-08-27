
from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20)
    user_pass = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    status = models.BooleanField(default='TRUE')
    borrower_name = models.CharField(max_length=50,default=None ,blank='True') 

    def __str__(self):
        return self.title