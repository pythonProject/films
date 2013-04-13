#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import template
from models import Genre

register = template.Library()

class GenresListNode():
    def __init__(self):
        pass

    def render(self, context):
#        g = Genre.objects.all().values()
        context["genres_list"] = Genre.objects.all().values()
#        context["genres_list"] =[g[i: i + 4] for i in range(0, len(g), 4)]
        return ""

@register.inclusion_tag("templates/base.html")
def genresList():
    return {
        "genres_list": Genre.objects.all().values(),
    }
