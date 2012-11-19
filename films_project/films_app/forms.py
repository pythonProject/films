#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from films_app.models import Genre, Author

class UploadFilmsForm(forms.Form):
    name = forms.CharField()
    director = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    link = forms.CharField()
    releaseDate = forms.DateTimeField(required=False)
    add_authors = forms.CharField(required=False)
    addGenre = forms.CharField(required=False)
    actors = forms.CharField(required=False)
    image = forms.ImageField()

class CreateAccount(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget = forms.PasswordInput())

class Log_in(forms.Form):
    login = forms.CharField(max_length = 30)
    password = forms.CharField(widget=forms.PasswordInput())

class Search(forms.Form):
    name = forms.CharField(required=False)
    add_authors = forms.CharField(required=False)
    actors = forms.CharField(required=False)
    director = forms.CharField(required=False)

