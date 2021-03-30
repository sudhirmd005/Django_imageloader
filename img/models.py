from django.db import models

# Create your models here.
class Imageloader(models.Model):
    photo = models.ImageField(upload_to="drive")
    date = models.DateTimeField(auto_now_add=True)

