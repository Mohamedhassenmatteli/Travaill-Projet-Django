from django.urls import path

from .views import *

app_name = "Vehicules"

urlpatterns = [
    path("", Liste_vehicules.as_view(), name="listview"),
    path("detail/<int:pk>/", Detail_vehicule.as_view(), name="detail"),
    path("ajouter/", Ajouter_vehicule.as_view(), name="add"),
    path("modifier/<int:pk>/", Modifier_vehicule.as_view(), name="update"),
    path("supprimer/<int:pk>/", Supprimer_vehicule.as_view(), name="delete"),
]