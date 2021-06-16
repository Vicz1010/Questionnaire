from django.db import models

# Create your models here.

class NewForm(models.Model):
    first_name = models.CharField(max_length= 128)
    last_name = models.CharField(max_length= 128)
    location = models.CharField(max_length= 128)
    job = models.CharField(max_length= 128)
