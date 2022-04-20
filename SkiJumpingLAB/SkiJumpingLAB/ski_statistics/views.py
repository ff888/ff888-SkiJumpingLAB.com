from django.shortcuts import render
from django.http import HttpResponse


def statistics(request):
    return HttpResponse('<h1>statistics</h1>')


def about(request):
    return HttpResponse('<h1>about</h1>')


def contact(request):
    return HttpResponse('<h1>contact</h1>')
