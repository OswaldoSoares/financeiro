""" Reusable functions. """

from itertools import groupby
from django.db.models import F, Sum
from django.http import JsonResponse
from transactions import models as md
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
        "payment__registry__date", "payment__registry__ordering"
    )
    return {"methods": methods}
