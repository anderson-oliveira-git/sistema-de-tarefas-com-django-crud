from django.db import models
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    data = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    status = models.CharField(max_length=30) 