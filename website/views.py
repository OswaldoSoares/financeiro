""" Encapsulate the logic responsible for processing a request """
from django.shortcuts import render


def index_website(request):
    context = {"nome": "Hello Word"}
    return render(request, "website/index.html", context)
