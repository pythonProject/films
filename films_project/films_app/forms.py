#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from films_app.models import Genre, Author

listOfGenres = {}

for d in Genre.objects.all().values_list():
	listOfGenres[d[0]] = d[1]

#authors = {}
#
#def addChoices(ch_id, ch_name):
#	authors[ch_id] = ch_name

class UploadFilmsForm(forms.Form):
	name = 	forms.CharField()
	director = forms.CharField()
	description = forms.CharField(widget=forms.Textarea)
	link = forms.CharField()
	releaseDate = forms.DateTimeField(required=False)
	add_authors = forms.CharField()
#	list_authors = forms.MultipleChoiceField(widget=CheckboxSelectMultiple, required = False, choices=authors.items())
	genre = forms.MultipleChoiceField(widget=CheckboxSelectMultiple, choices=listOfGenres.items())
	addGenre = forms.CharField(required=False)
	actors = forms.CharField()

class CreateAccount(forms.Form):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField()
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget = forms.PasswordInput())

class Log_in(forms.Form):
    login = forms.CharField(max_length = 30)
    password = forms.CharField(widget=forms.PasswordInput())