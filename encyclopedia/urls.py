from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entries, name="entries"),
    path("search", views.search, name="search"),
    path("new", views.new_entry, name="new"),
]
