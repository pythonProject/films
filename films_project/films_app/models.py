from django.db import models

class Films(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=400)
    user = models.IntegerField()
    release_date = models.DateField()
    added_date = models.DateField(auto_now_add=True)

class Author(models.Model):
    name = models.CharField(max_length=50)
    filmography = models.ManyToManyField(Films)

class genre(models.Model):
    name = models.CharField(max_length=30)
    film = models.ManyToManyField(Films)

class Actors(models.Model):
    name = models.CharField(max_length=30)
    filmography = models.ManyToManyField(Films)
    