#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

class UploadFilmsForm(forms.Form):
	name = 	forms.CharField()
	director = forms.CharField()
	description = forms.CharField()
	link = forms.CharField()
	releaseDate = forms.DateTimeField()
	authors = forms.CharField()
	genre = forms.CharField()
	actors = forms.CharField()