#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UploadFilmsForm
from films_app.models import Films, Author, Genre, Actors
import 


def hello(request):
	return render_to_response("hello.html", {"hello": "hello"})

def reqMeta(request):
	# import ipdb; ipdb.set_trace()
	res = request.META.items()
	return render_to_response("meta.html", {"res": res})

def UploadForm(request):
	form = UploadFilmsForm()
	if request.method == "POST":
		form = UploadFilmsForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			# form = Films(name = cd["name"], 
			# 			director = cd["director"], 
			# 			description = cd["description"], 
			# 			link = cd["link"], 
			# 			release_date = cd["releaseDate"],
			# 			added_date = )
			pass
	# form = UploadFilmsForm(
	# 					initial = {"name": "anymals"}
	# 					)
	return render_to_response("uploadFilm.html", {"form": form}, context_instance=RequestContext(request))
