#!/usr/bin/python
# -*- coding: utf-8 -*-

from films_app.models import Genre, Author, Actors, Films
from films_app.forms import Search
from films_app.views import CheckSearch

def genre_list(request):
    authors = Author.objects.values("name")
    actors = Actors.objects.values("name")
    search_form = Search()
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
    search = True if CheckSearch(request) else False
    return {"GENRE_LIST": Genre.objects.all(),
            "user": request.user,
            "search_form": search_form,
            "release_dates": release_dates,
            "release_date_max": release_date_max,
            "release_date_min": release_date_min,
            "authors": authors,
            "search": search,
            "actors":actors,
            "request": request}
