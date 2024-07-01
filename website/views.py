""" Encapsulate the logic responsible for processing a request """
from django.shortcuts import render
from monetary.models import Accounts


def index_website(request):
    context = {"nome": "Hello Word"}
    return render(request, "website/index.html", context)
