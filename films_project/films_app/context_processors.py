#!/usr/bin/python
# -*- coding: utf-8 -*-

from films_app.models import Genre

def genre_list(request):
    return {"GENRE_LIST": Genre.objects.all(),
            "user": request.user}
