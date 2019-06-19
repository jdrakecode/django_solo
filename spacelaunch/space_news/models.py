from django.db import models

# Create your models here.

class News(models.Model):
    # title = models.CharField(max_length=50)
    date = models.DateField()
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=1500)

    def __str__(self):
        return self.name

class Launches(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    payload = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    site = models.CharField(max_length=150)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.name
