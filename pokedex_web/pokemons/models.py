from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    abilities = models.CharField(max_length=255)
    forms = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    stats = models.TextField()
    image_url = models.URLField(max_length=255)