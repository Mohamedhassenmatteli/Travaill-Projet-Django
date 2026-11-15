from django.urls import path
from .models  import offre
from .views import *

app_name = "Offre"

urlpatterns = [
    path("list/",ListOffre.as_view(),name="listview"),
    path("detail/<int:pk>/",DetailOffre.as_view(),name="detailview"),
    path("create",CreateOffre.as_view(),name="createview"),
    path("update/<int:pk>/",UpdateOffre.as_view(),name="updateview"),
    path("delete/<int:pk>/",deleteOffre.as_view(),name="deleteview"),
]