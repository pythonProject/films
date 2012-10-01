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