#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UploadFilmsForm, CreateAccount
from films_app.models import Films, Author, Genre, Actors
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def CreateUser(request):
	createAccountForm = CreateAccount()
	if request.method == "Post":
		createAccountForm = CreateAccount(request.POST)
		if createAccountForm.is_valid():
			cd = createAccountForm.cleaned_data
			user = User.objects.create_user(first_name = cd["first_name"],
											last_name = cd["last_name"],
											email = cd["email"],
											username = cd["username"],
											password = cd["password"])
			user.save()
			return HttpResponseRedirect("/thanks/")
	return render_to_response("createAccount.html", {"form": createAccountForm}, context_instance=RequestContext(request))

def Thanks(request):
	return render_to_response("thanks.html")

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
