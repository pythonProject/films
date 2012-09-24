#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

def hello(request):
	return render_to_response("hello.html", {"hello": "hello"})

def reqMeta(request):
	# import ipdb; ipdb.set_trace()
	res = request.META.items()
	return render_to_response("meta.html", {"res": res})
