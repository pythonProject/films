#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import CheckboxSelectMultiple

listOfGenres = (("oleh1", "OLEH1"),
					("oleh2", "OLEH2"),
					("oleh3", "OLEH3"),
					("oleh4", "OLEH4"))

class UploadFilmsForm(forms.Form):
	name = 	forms.CharField()
	director = forms.CharField()
	description = forms.CharField(widget=forms.Textarea)
	link = forms.CharField()
	releaseDate = forms.DateTimeField(required=False)
	authors = forms.CharField()
	genre = forms.MultipleChoiceField(widget=CheckboxSelectMultiple, choices=listOfGenres)
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