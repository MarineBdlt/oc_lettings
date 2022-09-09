from django.shortcuts import render


def index(request):
    return render(request, "index.html")


from django.urls import path


def trigger_error(request):
    division_by_zero = 1 / 0
