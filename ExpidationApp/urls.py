from .views import *
from django.urls import path


app_name = "Expidation"
urlpatterns = [
    path('home/',home,name="home"),
    path('w/<str:name>/',welcome,name="welcomeFunction"),
    path('list/', ListExpidation, name="list"),
    path('detail/<str:reference>/',detailExpidation,name="detail"),
    path('delete/<str:reference>/',deleteExpidation,name="delete"),
    path('listview/',Liste_expidation.as_view(),name="listview"),
    path('detailview/<str:pk>/',detail_expidation.as_view(),name="detailview"),
    path('deleteclass/<str:pk>/',delete_expidation.as_view(),name="deleteview"),
    path("add/",Ajouter_Expedition.as_view(),name="add"),
    path("update/<str:pk>/",Update_Expedition.as_view(),name="update")
]
