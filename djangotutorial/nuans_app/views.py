# from django.shortcuts import render

# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import render, get_object_or_404 # type: ignore
from django.conf import settings # type: ignore
import os

def hakk(request):
    return render(request, 'hakk.html')


def blogs(request):
    return render(request, 'blogs.html')


def contact(request):
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'contact.html',context)


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')