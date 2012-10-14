#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UploadFilmsForm, CreateAccount, Log_in
from films_app.models import Films, Author, Genre, Actors
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django.contrib import auth
import datetime

def RequiresLogin(view):
    def check(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/login/")
        return view(request, *args, **kwargs)
    return check


def Index(request):
    if request.session and request.GET.get('quit', False):
        auth.logout(request)
    form = Log_in()
    return render_to_response("index.html", {"form": form}, context_instance=RequestContext(request))

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
                user = auth.authenticate(username = cd["username"], password = cd["password"])
                auth.login(request, user)
                return HttpResponseRedirect("/logged_in/")
        except IntegrityError:
            err = "Извините, данный логин уже используеться!"
            return render_to_response("createAccount.html", {"form": createAccountForm, "err": err}, context_instance=RequestContext(request))
        # return HttpResponseRedirect("/logged_in/")
    return render_to_response("createAccount.html", {"form": createAccountForm}, context_instance=RequestContext(request))

def Logged_in(request):
    return render_to_response("logged_in.html", context_instance=RequestContext(request))

def LoginView(request):
    form = Log_in()
    if request.method == "POST":
        form = Log_in(request.POST)
        if form.is_valid():
            user = auth.authenticate(username = request.POST["login"], password = request.POST["password"])
            if user is not None:
                request.session["user"] = request.POST["login"]
                auth.login(request, user)
                return HttpResponseRedirect("/logged_in/")
            else:
                error = 2
                return render_to_response("login.html", {"form": form, "error": error}, context_instance=RequestContext(request))
    return render_to_response("login.html", {"form": form}, context_instance=RequestContext(request))

def Thanks(request):
    return render_to_response("thanks.html")

def UploadForm(request):
    authors_list = []
    list_genres = []
    actors_list = []
    for a in Actors.objects.all().values_list():
        actors_list.append(a[1])
    for d in Author.objects.all().values_list():
        authors_list.append(d[1])
    for g in Genre.objects.all().values_list():
        list_genres.append(g[1])
    form = UploadFilmsForm()
    if request.method == "POST":
        form = UploadFilmsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # film = Films(name = cd["name"],
            # 			director = cd["director"],
            # 			description = cd["description"],
            # 			link = cd["link"],
            # 			user = int(User.objects.get(username = request.session["user"])),
            # 			release_date = cd.get("release_date", False),
            # 			)
            # author = Author(name = )
    #	if request.is_ajax():
    #		if request.method == "POST" and request.POST["name"]:
    #			addChoices(request.POST["id"], request.POST["name"])
    #			import  ipdb; ipdb.set_trace()
    #			return HttpResponse(form.fields["list_authors"])
    return render_to_response("uploadFilm.html", {"form": form,
                                                  "authors_list": authors_list,
                                                  "list_genres": list_genres,
                                                  "actors_list": actors_list},
                                    context_instance=RequestContext(request))
