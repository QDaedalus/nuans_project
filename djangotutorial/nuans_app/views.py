# from django.shortcuts import render

# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import render, get_object_or_404 # type: ignore


def about(request):
    return render(request, 'about.html')


def blogs(request):
    return render(request, 'blogs.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')