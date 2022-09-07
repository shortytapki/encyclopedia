from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.entry, name="entry"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("create", views.create_page, name="create_page"),
    path("publish", views.publish_new_page, name="publish_new_page")
]
