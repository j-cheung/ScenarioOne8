from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. We are team 8, we all obey Anita")

# Create your views here.

