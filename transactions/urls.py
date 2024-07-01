from django.urls import path
from transactions.views import (
    index_transactions,
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
        "add_payment",
        add_payment,
        name="add_payment",
    ),
    path(
        "add_registry",
        add_registry,
        name="add_registry",
    ),
]
