from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.entry, name="entry"),
    path("random", views.random, name="random")
    # path("/?q=", views.search, name="search")
]
