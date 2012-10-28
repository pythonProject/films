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
from django.utils import simplejson
from films_project import settings

def RequiresLogin(view):
    def check(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/login/")
        return view(request, *args, **kwargs)
    return check


def Index(request):
    page1 = 0
    page2 = 0
    if request.session and request.GET.get('quit', False):
        auth.logout(request)
    if not request.GET.get('page', False) or request.GET.get("page", False) == 1:
        try:
            if int(Films.objects.order_by("-id")[0].id) < 10:
                page2 = int(Films.objects.order_by("-id")[0].id)
            else:
                page2 = 10
        except IndexError:
            pass
    films_list = Films.objects.all()[page1:page2]
    for i in films_list:
        i.release_date = str(i.release_date.year) + "-" + str(i.release_date.month)+ "-" + str(i.release_date.day)
    form = Log_in()
    return render_to_response("index.html", {"form_login": form,
                                             "films_list": films_list}, context_instance=RequestContext(request))

def CreateUser(request):
    createAccountForm = CreateAccount()
    form_login = Log_in()
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
                request.session["user"] = request.POST["username"]
                return HttpResponseRedirect("/logged_in/")
        except IntegrityError:
            err = "Извините, данный логин уже используеться!"
            return render_to_response("createAccount.html", {"form": createAccountForm, "err": err}, context_instance=RequestContext(request))
    return render_to_response("createAccount.html", {"form": createAccountForm, "form_login": form_login}, context_instance=RequestContext(request))

def Logged_in(request):
    return render_to_response("logged_in.html", context_instance=RequestContext(request))

def LoginAjax(request):
    res = {}
    res["error"] = False
    if request.is_ajax():
        if request.method == "POST":
            form = Log_in(request.POST)
            if form.is_valid():
                user = auth.authenticate(username=request.POST["login"], password=request.POST["password"])
                if user is not None:
                    request.session["user"] = request.POST["login"]
                    auth.login(request, user)
                else:
                    res["error"] = True
    return HttpResponse(simplejson.dumps(res), mimetype='application/json')


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
                return render_to_response("login.html", {"form": form, "error": error},
                                            context_instance=RequestContext(request))
    return render_to_response("login.html", {"form": form}, context_instance=RequestContext(request))

def Thanks(request):
    return render_to_response("thanks.html")

def devideGenres(genre):
    return genre.split("_")[1]

def devideAuthors(author):
    return author.split("_")[1]

def devideActors(actor):
    return actor.split("_")[1]

def UploadForm(request):
    authors_list = []
    list_genres = []
    actors_list = []
    genre = []
    author = []
    actor = []
    for a in Actors.objects.all().values_list():
        actors_list.append(a[1])
    for d in Author.objects.all().values_list():
        authors_list.append(d[1])
    for g in Genre.objects.all().values_list():
        list_genres.append(g[1])
    form = UploadFilmsForm()
    if request.method == "POST":
        form = UploadFilmsForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if not cd["releaseDate"]:
                cd["releaseDate"] = "1000-01-01"
            else:
                cd["releaseDate"] = cd["releaseDate"].strftime("%Y-%m-%d")
            film = Films(name = cd["name"],
                        director = cd["director"],
                        description = cd["description"],
                        link = cd["link"],
                        user = int(User.objects.filter(username = request.session["user"]).values("id")[0]["id"]),
                        release_date = cd["releaseDate"],
                        added_date = datetime.datetime.now().strftime("%Y-%m-%d"),
                        image = request.FILES["image"],
                        )
            film.save()
            for i in request.POST.items():
                if i[1] == "on":
                    if "author" in i[0]:
                        author_temp = Author.objects.filter(name = i[0].split("_")[1].strip())
                        if author_temp:
                            author.append(author_temp.values_list()[0][0])
                        else:
                            author_temp = Author(name = i[0].split("_")[1].strip())
                            author_temp.save()
                            author.append(author_temp.id)
                    elif "genre" in i[0]:
                        genre_tmp = Genre.objects.filter(name = i[0].split("_")[1])
                        genre.append(genre_tmp.values_list()[0][0])
                    else :
                        actor_temp = Actors.objects.filter(name = i[0].split("_")[1].strip())
                        if actor_temp:
                            actor.append(actor_temp.values_list()[0][0])
                        else:
                            actor_temp = Actors(name = i[0].split("_")[1].strip())
                            actor_temp.save()
                            actor.append(actor_temp.id)
            film.genre.add(*genre)
            film.authors.add(*author)
            film.actors.add(*actor)
            return HttpResponseRedirect("/uploaded/")
    return render_to_response("uploadFilm.html", {"form": form,
                                                  "authors_list": authors_list,
                                                  "list_genres": list_genres,
                                                  "actors_list": actors_list},
                                    context_instance=RequestContext(request))

def uploaded(request):
    return render_to_response("uploaded.html")