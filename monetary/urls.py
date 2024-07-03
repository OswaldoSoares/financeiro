from django.urls import path
from monetary.views import (
    add_transfer,
    index_monetary,
)


urlpatterns = [
    path(
        "index_monetary",
        index_monetary,
        name="index_monetary",
    ),
]
