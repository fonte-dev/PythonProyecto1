from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.lista_familiares, name="lista_familiares"),
]
