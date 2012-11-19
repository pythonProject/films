from django.db import models
from signals import makeThumbnails

class Author(models.Model):
    name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=30)

class Actors(models.Model):
    name = models.CharField(max_length=30)

class Films(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=400)
    user = models.IntegerField()
    release_date = models.DateField()
    added_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    authors = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actors)

models.signals.post_save.connect(makeThumbnails, sender=Films)