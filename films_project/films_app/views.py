#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render
from django.template import RequestContext
from forms import UploadFilmsForm, CreateAccount, Log_in, Search
from films_app.models import Films, Author, Genre, Actors
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django.contrib import auth
import datetime
from django.utils import simplejson
from django.core.cache import cache

def RequiresLogin(view):
    def check(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/login/")
        return view(request, *args, **kwargs)
    return check

def FilmsList(request, films_on_page = 10):
    try:
        films_count = Films.objects.order_by("-id")[0].id
    except IndexError:
        films_count = 0
    if films_count > films_on_page and request.GET.get("page") and int(request.GET.get("page", False)) != 1:
        films_list = Films.objects.all()[int(request.GET.get("page", False)) * films_on_page - films_on_page:
                                         int(request.GET.get("page", False)) * films_on_page ]
    else:
        films_list = Films.objects.all()[:films_on_page]
    return films_list, range((films_count / films_on_page) + 1 if films_count % films_on_page == 0 \
                                                   else (films_count / films_on_page) + 2), False

def search_func(request, films_on_page = 10):
    if request.GET.get("page", False) and int(request.GET.get("page", False)) != 1:
        query_page = "[int(request.GET.get('page', False)) * films_on_page - films_on_page:int(request.GET.get('page', False)) * films_on_page ]"
    else:
        query_page = "[:films_on_page]"
    search_query = "Films.objects"
    search_form = Search(request.GET)
    if search_form.is_valid():
        form = search_form.cleaned_data
    if form["name"] != "":
        search_query += ".filter(name='" + form["name"].strip() + "')"
    if form["director"] != "":
        search_query += ".filter(director='" + form["director"].strip() + "')"
    for item in request.GET:
        if "author_" in item:
            search_query += ".filter(authors__name__exact='" + devideAuthors(item).strip() + "')"
        if "actor_" in item:
            search_query += ".filter(actors__name__exact='" + devideActors(item).strip() + "')"
    if "genre" in request.GET:
        search_query += ".filter(genre__name='" + request.GET["genre"] + "')"
    if "start_date" in request.GET:
        search_query += ".filter(release_date__range=('"+ request.GET["start_date"] + "-01-01','" + request.GET["end_date"] + "-12-31'))"
    films_list = eval(search_query + query_page)
    films_count = eval(search_query).count()
    return films_list, range((films_count / films_on_page) + 1 if films_count % films_on_page == 0\
                                                               else (films_count / films_on_page) + 2), True

def CheckSearch(request):
    for item in request.GET:
        if "actor_" in item:
            return True
        if "author_" in item:
            return True
    if "name" in request.GET:
        return True
    if "director" in request.GET:
        return True
    if "genre" in request.GET:
        return True
    return False

def getGenresList():
    g = Genre.objects.all().values()
    return [g[i: i + 4] for i in range(0, len(g), 4)]

def Index(request):
    authors = Author.objects.values("name")
    actors = Actors.objects.values("name")
    search_form = Search()
    films_on_page = 2
    release_dates = []
    release_dates_original = Films.objects.values("release_date")
    for i in release_dates_original:
        if i["release_date"].year not in release_dates:
            release_dates.append(i["release_date"].year)
    try:
        release_date_min = release_dates[0]
        release_date_max = release_dates[0]
    except IndexError:
        release_date_max = "0"
        release_date_min = "0"
    for release_date in release_dates:
        if release_date > release_date_max:
            release_date_max = release_date
        if release_date < release_date_min:
            release_date_min = release_date
    if request.session and request.GET.get('quit', False):
        auth.logout(request)
    if CheckSearch(request):
        films_list, page_count, search = search_func(request, films_on_page)
    else:
        if request.GET.get("search", False):
            if request.GET.get("page", False) and int(request.GET.get("page", False)) != 1:
                films_list = request.session["search_res"][int(request.GET.get('page', False)) * films_on_page - films_on_page:int(request.GET.get('page', False)) * films_on_page ]
            else:
                films_list = request.session["search_res"][:films_on_page]
            page_count = range((request.session["films_count"] / films_on_page) + 1 if request.session["films_count"] % films_on_page == 0\
                                                else (request.session["films_count"] / films_on_page) + 2)
        else:
            films_list, page_count, search = FilmsList(request, films_on_page = films_on_page)
    for i in films_list:
        i.release_date = str(i.release_date.year) + "-" + str(i.release_date.month)+ "-" + str(i.release_date.day)
    form = Log_in()
    return render(request, "index.html", {"form_login": form,
                                             "films_list": films_list,
                                             "page_count": page_count,
                                             "search_form": search_form,
                                             "release_dates": release_dates,
                                             "release_date_max": release_date_max,
                                             "release_date_min": release_date_min,
                                             "authors": authors,
                                             "search": search,
                                             "actors":actors})

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
    return render(request, "createAccount.html", {"form": createAccountForm, "form_login": form_login})

def Logged_in(request):
    return render(request, "logged_in.html")

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
    return render(request, "login.html", {"form": form})

def Thanks(request):
    return render(request, "thanks.html")

def devideGenres(genre):
    return genre.split("_")[1]

def devideAuthors(author):
    return author.split("_")[1]

def devideActors(actor):
    return actor.split("_")[1]

def UploadForm(request):
    authors_list = []
    actors_list = []
    genre = []
    author = []
    actor = []
    for a in Actors.objects.all().values_list():
        actors_list.append(a[1])
    for d in Author.objects.all().values_list():
        authors_list.append(d[1])
    list_genres = getGenresList()
    form = UploadFilmsForm()
    if request.method == "POST":
        form = UploadFilmsForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if not cd["releaseDate"]:
                cd["releaseDate"] = "1000-01-01"
            else:
                cd["releaseDate"] = datetime.date(cd["releaseDate"].year, cd["releaseDate"].month, cd["releaseDate"].day).strftime("%Y-%m-%d")
            film = Films(name = cd["name"],
                        director = cd["director"],
                        description = cd["description"],
                        link = cd["link"],
                        user = int(User.objects.filter(username = request.session["user"]).values("id")[0]["id"]),
                        release_date = cd["releaseDate"],
                        added_date = datetime.datetime.now().strftime("%Y-%m-%d"),
                        image = request.FILES["image"],
                        content = request.FILES["content"],
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
    return render(request, "uploadFilm.html", {"form": form,
                                                  "authors_list": authors_list,
                                                  "list_genres": list_genres,
                                                  "actors_list": actors_list})

def uploaded(request):
    return render(request, "uploaded.html")