from django.db import models

# Create your models here.

class Requests(models.Model):
    name = models.CharField(max_length=255)