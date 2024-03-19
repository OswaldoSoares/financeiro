""" Reusable functions. """

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
