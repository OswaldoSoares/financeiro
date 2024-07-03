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


def save_transfer(request):
    record = []
    out_account = request.POST.get("out_account")
    in_account = request.POST.get("in_account")
    input_value = float(request.POST.get("value"))
    record.append(
        md.Transfers(
            out_account_id=out_account,
            in_account_id=in_account,
            value=input_value,
            date=request.POST.get("date"),
        )
    )
    md.Transfers.objects.bulk_create(record)
    save_new_balance(out_account, input_value, "minus")
    save_new_balance(in_account, input_value, "plus")
