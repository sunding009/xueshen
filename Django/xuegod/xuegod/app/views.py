# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response


def welcome(request):
    return HttpResponse("Welcome!")


def index(request):
    return HttpResponse("Index!")


def hello(request):
    return HttpResponse("Hello!")


def hi(request, name, age):
    return HttpResponse("I am {0}, This is my {1} years old.".format(name, age))


def happy(request):
    # template = get_template("happy.html")
    # contex = Context({"name": "sunding", "age": 18})
    # print "-"*100, contex
    # # html = template.render(contex)
    # return HttpResponse(template.render(contex[1]))

    return render_to_response("happy.html", {"name": "sunding", "age": 18})