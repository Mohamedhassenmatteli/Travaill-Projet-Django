from .views import *
from django.urls import path


app_name = "Expidation"
urlpatterns = [
    path('home/',home,name="home"),
    path('w/<str:name>/',welcome,name="welcomeFunction"),
    path('list/', ListExpidation, name="list"),
    path('detail/<str:reference>/',detailExpidation,name="detail"),
    path('delete/<str:reference>/',deleteExpidation,name="delete")
]
