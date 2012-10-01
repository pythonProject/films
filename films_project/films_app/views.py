#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UploadFilmsForm, CreateAccount, Log_in
from films_app.models import Films, Author, Genre, Actors
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.contrib import auth

def Index(request):
    if request.session:
        auth.logout(request)
    return render_to_response("index.html")

def CreateUser(request):
    createAccountForm = CreateAccount()
    if request.method == "POST":
		try:
			createAccountForm = CreateAccount(request.POST)
			if createAccountForm.is_valid():
				cd = createAccountForm.cleaned_data
				account = User.objects.create_user(cd["username"], cd["email"], cd["password"])
				account.first_name = cd["first_name"]
				account.last_name = cd["last_name"]
				account.save()
		except IntegrityError:
			err = "Извините, данный логин уже используеться!"
			return render_to_response("createAccount.html", {"form": createAccountForm, "err": err}, context_instance=RequestContext(request))
		return HttpResponseRedirect("/thanks/")
    return render_to_response("createAccount.html", {"form": createAccountForm}, context_instance=RequestContext(request))

def Logged_in(request):
    if not request.user.is_authenticated():
        error = 1
        return render_to_response("error.html", {"error": error})
    var = request.session
    return render_to_response("logged_in.html", {"var": var})

def LoginView(request):
    form = Log_in()
    if request.method == "POST":
        form = Log_in(request.POST)
        if form.is_valid():
            user = auth.authenticate(username = request.POST["login"], password = request.POST["password"])
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect("/logged_in/")
            else:
                error = 2
                return render_to_response("login.html", {"form": form, "error": error}, context_instance=RequestContext(request))
    return render_to_response("login.html", {"form": form}, context_instance=RequestContext(request))





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
