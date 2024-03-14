from django.urls import path
from website.views import (index_website,)


urlpatterns = [
    path("", index_website, name="index_website",),

]
