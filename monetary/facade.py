from django.template.loader import render_to_string
from django.http import JsonResponse
from monetary import forms as fr
from monetary import models as md


def form_transfers(request):
    form = fr.TransferForm()
    context = {"form": form}
    data = {}
    data["html_modal"] = render_to_string(
        "monetary/modal_form_transfer.html", context, request=request
    )
    return JsonResponse(data)
