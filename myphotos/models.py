from django.db import models

# Create your models here.
class Photos(models.Model):
    docfile = models.FileField(upload_to='photos/%Y/%m/%d')