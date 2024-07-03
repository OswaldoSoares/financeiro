from django.shortcuts import render
from transactions import facade as tf
from website import facade as wf


def index_transactions(request):
    month_year = request.GET.get("date")
    if month_year is None:
        month, year = wf.today_month_year()
        month_year = f"{month}/{year}"
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
        data = tf.form_regitries(request)
    else:
        tf.save_registry(request)
        context = tf.create_registries_context_unpayd()
        data = tf.create_registries_data_unpaid(request, context)
    return data


def add_registry_itens(request):
    if request.method == "GET":
        print(request.GET)
        data = tf.form_registry_itens(request)
    else:
        tf.save_reguistry_item(request)
        context = tf.create_registry_itens_context(
            request.POST.get("registry_id")
        )
        data = tf.create_registry_itens_data(request, context)
        print(request.POST)
    return data


def add_payment(request):
    if request.method == "GET":
        if tf.consult_payment(request.GET.get("id_selected")):
            print("OK")
        else:
            print(request.GET)
            data = tf.form_payment(request)
    else:
        tf.save_payment(request)
        print(request.POST)
    return data


def view_registry_itens(request):
    context = tf.create_registry_itens_context(request.GET.get("registry_id"))
    data = tf.create_registry_itens_data(request, context)
    return data


def add_company(request):
    if request.method == "GET":
        data = tf.form_companies(request)
    else:
        tf.save_company(request)
        data = tf.create_company_data_message(request)
    return data


def add_category(request):
    if request.method == "GET":
        data = tf.form_categories(request)
    else:
        tf.save_category(request)
        data = tf.create_category_data_message(request)
    return data
