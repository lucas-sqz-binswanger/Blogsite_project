from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_image', blank=True)
    studio = models.CharField(max_length=100)
    released = models.CharField(max_length=30)
    synopsis = models.TextField()
    my_thoughts = models.TextField()


class Vaccine(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
