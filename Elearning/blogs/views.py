from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "blogs/index.html")


def show(request):
    return render(request, "blogs/show.html")
