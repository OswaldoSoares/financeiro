from django.shortcuts import render
from monetary import facade as mf

# Create your views here.


def index_monetary(request):
    context = {"nada": "nada"}
    return render(request, "monetary/index_monetary.html", context)


def add_transfer(request):
    if request.method == "GET":
        data = mf.form_transfers(request)
    else:
        mf.save_transfer(request)
        data = mf.create_transfer_data_message(request)
    return data
