from django.urls import path
from transactions.views import (
    index_transactions,
    add_category,
    add_company,
    add_payment,
    add_registry,
    add_registry_itens,
    view_registry_itens,
)


urlpatterns = [
    path(
        "",
        index_transactions,
        name="index_transactions",
    ),
    path(
        "add_category",
        add_category,
        name="add_category",
    ),
    path(
        "add_company",
        add_company,
        name="add_company",
    ),
    path(
        "add_payment",
        add_payment,
        name="add_payment",
    ),
    path(
        "add_registry",
        add_registry,
        name="add_registry",
    ),
    path(
        "add_registry_itens",
        add_registry_itens,
        name="add_registry_itens",
    ),
    path(
        "view_registry_itens",
        view_registry_itens,
        name="view_registry_itens",
    ),
]
