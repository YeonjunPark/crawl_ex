from django.db import models

class Graduate_school(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

class Title(models.Model):
    title = models.CharField(max_length=100)