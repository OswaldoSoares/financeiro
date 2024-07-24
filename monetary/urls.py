from django.urls import path
from monetary.views import (
    add_account,
    add_transfer,
    index_monetary,
)


urlpatterns = [
    path(
        "add_account",
        add_account,
        name="add_account",
    ),
    path(
        "add_transfer",
        add_transfer,
        name="add_transfer",
    ),
    path(
        "index_monetary",
        index_monetary,
        name="index_monetary",
    ),
]
