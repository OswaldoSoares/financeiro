from django.shortcuts import render
from monetary import facade as mf

# Create your views here.


def index_monetary(request):
    context = {"nada": "nada"}
    return render(request, "monetary/index_monetary.html", context)
