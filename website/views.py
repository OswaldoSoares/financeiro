""" Encapsulate the logic responsible for processing a request """
from django.shortcuts import render
from monetary.models import Accounts


def index_website(request):
    accounts = Accounts.objects.all()
    context = {"accounts": accounts}
    return render(request, "website/index.html", context)
