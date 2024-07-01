""" Reusable functions. """

from itertools import groupby
from django.db.models import F, Sum
from django.http import JsonResponse
from django.template.loader import render_to_string
from transactions import models as md
from transactions import forms as fr
from website import facade as website_facade


def create_registries_context_period(month_year):
    """
        Creates a context with registries by period.
    Args:
        month_year: Month and year used as the basis of the period.

    Returns:
        Context registries queryset

    """
    first_day, last_day = website_facade.start_end_dates(month_year)
    registries = md.Registries.objects.filter(
        date__range=[first_day, last_day]
    ).order_by("date")
    return {"registries": registries}


def create_registries_context_period_paid(month_year):
    """
        Creates a context with registries payments by period.
    Args:
        month_year: Month and year used as the basis of the period.

    Returns:
        Context payments queryset

    """
    first_day, last_day = website_facade.start_end_dates(month_year)
    payments = md.Payments.objects.filter(
        date__range=[first_day, last_day]
    ).order_by("date")
    return {"payments": payments}


def create_registries_context_period_paid_methods(month_year):
    """
        Creates a context with payment methods for records by period.
    Args:
        month_year: Month and year used as the basis of the period.

    Returns:
        Context methods queryset

    """
    first_day, last_day = website_facade.start_end_dates(month_year)
    methods = md.Methods.objects.filter(
        payment__date__range=[first_day, last_day]
    )
    return {"methods": methods}


def create_registries_context_period_paid_methods_unique(month_year):
    """
        Creates a context with payment methods for records by period.
        Removing equal payments.
    Args:
        month_year: Month and year used as the basis of the period.

    Returns:
        Context methods queryset

    """
    first_day, last_day = website_facade.start_end_dates(month_year)
    methods = list(
        md.Methods.objects.filter(
            payment__date__range=[first_day, last_day]
        ).values()
    )
    payments_distinct = list(
        {v["payment_id"]: v["id"] for v in methods}.values()
    )
    methods = md.Methods.objects.filter(id__in=payments_distinct).order_by(
        "-payment__date", "-payment__registry__ordering"
    )
    return {"methods": methods}
def create_category_n3_context_period_payd_methods_in(month_year):
    first_day, last_day = website_facade.start_end_dates(month_year)
    methods = list(
        md.Methods.objects.filter(
            payment__date__range=[first_day, last_day],
            payment__registry__in_out=True,
        )
        .annotate(category=F("payment__registry__category_n3__description"))
        .values("category", "value")
    )
    list_category = []
    for key, value in groupby(
        sorted(methods, key=lambda cat: cat["category"]),
        lambda cat: cat["category"],
    ):
        list_category.append(
            {
                "category": key,
                "value": str(sum(item["value"] for item in list(value))),
            }
        )
    return {"category_n3_in": list_category}


def create_category_n2_context_period_payd_methods_out(month_year):
    first_day, last_day = website_facade.start_end_dates(month_year)
    methods = list(
        md.Methods.objects.filter(
            payment__date__range=[first_day, last_day],
            payment__registry__in_out=False,
        )
        .annotate(category=F("payment__registry__category_n2__description"))
        .values("category", "value")
    )
    list_category = []
    for key, value in groupby(
        sorted(methods, key=lambda cat: cat["category"]),
        lambda cat: cat["category"],
    ):
        list_category.append(
            {
                "category": key,
                "value": str(sum(item["value"] for item in list(value))),
            }
        )
    return {"category_n2_out": list_category}


def create_category_n3_context_period_payd_methods_out(month_year):
    first_day, last_day = website_facade.start_end_dates(month_year)
    methods = list(
        md.Methods.objects.filter(
            payment__date__range=[first_day, last_day],
            payment__registry__in_out=False,
        )
        .annotate(category=F("payment__registry__category_n3__description"))
        .values("category", "value")
    )
    list_category = []
    for key, value in groupby(
        sorted(methods, key=lambda cat: cat["category"]),
        lambda cat: cat["category"],
    ):
        list_category.append(
            {
                "category": key,
                "value": str(sum(item["value"] for item in list(value))),
            }
        )
    return {"category_n3_out": list_category}


def create_payment_context_unmethod(month_year):
    first_day, last_day = website_facade.start_end_dates(month_year)
    methods = md.Methods.objects.filter(
        payment__date__range=[first_day, last_day]
    )
    list_id = []
    for method in methods:
        list_id.append(method.payment_id)
    unmethods = md.Payments.objects.all().exclude(id__in=list_id)
    return {"unmethods": unmethods}


def create_registries_context_unpayd():
    payds = md.Payments.objects.all()
    list_id = []
    for payd in payds:
        list_id.append(payd.registry_id)
    unpaids = md.Registries.objects.all().exclude(id__in=list_id)
    return {"unpaids": unpaids}


def create_registry_itens_context(registry_id):
    itens = md.RegistryItens.objects.filter(registry_id=registry_id).annotate(
        total=Sum(F("amount") * F("unitary"))
    )
    total = itens.aggregate(value=Sum("total"))
    return {"itens": itens, "total": total, "registry_id": registry_id}


def create_registries_data_unpaid(request, context):
    data = {}
    data["html_registries_unpaid"] = render_to_string(
        "transactions/card_registries_unpaid.html", context, request=request
    )
    return JsonResponse(data)


def create_registry_itens_data(request, context):
    data = {}
    data["html_registry_itens"] = render_to_string(
        "transactions/card_registry_itens.html", context, request=request
    )
    return JsonResponse(data)


def form_payment(request):
    registry = md.Registries.objects.get(id=request.GET.get("id_selected"))
    print(registry)
    form = fr.PaymentForm()
    context = {"form": form, "registry": registry}
    data = {}
    data["html_modal"] = render_to_string(
        "transactions/modal_form_payment.html", context, request=request
    )
    return JsonResponse(data)


def form_regitries(request):
    form = fr.RegistriesForm()
    context = {"form": form}
    data = {}
    data["html_modal"] = render_to_string(
        "transactions/modal_form_registry.html", context, request=request
    )
    return JsonResponse(data)


def form_registry_itens(request):
    registry = md.Registries.objects.get(id=request.GET.get("id_selected"))
    form = fr.RegistryItensForm()
    context = {"form": form, "registry": registry}
    data = {}
    data["html_modal"] = render_to_string(
        "transactions/modal_form_registry_item.html", context, request=request
    )
    return JsonResponse(data)


def save_registry(request):
    record = []
    record.append(
        md.Registries(
            date=request.POST.get("date"),
            companies_id=int(request.POST.get("companies")),
            category_n1_id=int(request.POST.get("category_n1")),
            category_n2_id=int(request.POST.get("category_n2")),
            category_n3_id=int(request.POST.get("category_n3")),
            value=request.POST.get("value"),
            in_out=True if request.POST.get("in_out") == "CRÉDITO" else False,
            ordering=request.POST.get("ordering"),
            obs=request.POST.get("obs"),
        )
    )
    md.Registries.objects.bulk_create(record)


def save_registry_item(request):
    record = []
    record.append(
        md.RegistryItens(
            description=request.POST.get("description").upper(),
            brand=request.POST.get("brand").upper(),
            amount=float(request.POST.get("amount")),
            unitary=float(request.POST.get("unitary")),
            favored=request.POST.get("favored").upper(),
            registry_id=int(request.POST.get("registry_id")),
        )
    )
    md.RegistryItens.objects.bulk_create(record)


def save_payment(request):
    record = []
    record.append(
        md.Payments(
            date=request.POST.get("date"),
            registry_id=int(request.POST.get("registry_id")),
        )
    )
    md.Payments.objects.bulk_create(record)


def save_method(request):
    record = []
    record.append(
        md.Methods(
            payment_id=int(request.POST.get("payment_id")),
            account_id=int(request.POST.get("account_id")),
            value=float(request.POST.get("value")),
        )
    )
    md.Methods.objects.bulk_create(record)


def consult_payment(registry_id):
    payment = md.Payments.objects.filter(registry_id=registry_id)
    if payment:
        return {"payment": payment}
    else:
        return False
