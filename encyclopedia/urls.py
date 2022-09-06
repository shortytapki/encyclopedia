from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.entry, name="entry"),
    path("random", views.random, name="random"),
    # path("search/", views.search, name="search"),
    path("wiki/search/", views.search, name="search")
]
