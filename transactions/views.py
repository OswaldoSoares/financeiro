from django.shortcuts import render
from transactions import facade as tf


def index_transactions(request):
    month_year = "04/2024"
    context = {}
    context.update(
        tf.create_registries_context_period_paid_methods_unique(month_year)
    )
    context.update(
        tf.create_category_n1_context_period_payd_methods(month_year)
    )
    context.update(
        tf.create_category_n2_context_period_payd_methods_in(month_year)
    )
    context.update(
        tf.create_category_n2_context_period_payd_methods_out(month_year)
    )
    context.update(
        tf.create_category_n3_context_period_payd_methods_in(month_year)
    )
    context.update(
        tf.create_category_n3_context_period_payd_methods_out(month_year)
    )
    context.update(tf.create_registries_context_unpayd())
    return render(request, "transactions/index_transactions.html", context)


def add_registry(request):
    if request.method == "GET":
        data = tf.form_regsitries(request)
    else:
        tf.save_registry(request)
        context = tf.create_registries_context_unpayd()
        data = tf.create_registries_data_unpaid(request, context)
    return data
