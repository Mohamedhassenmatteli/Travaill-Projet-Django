from django.http import HttpResponse
from .models import expedition
from django.shortcuts import get_object_or_404, render

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the django project</h1>")


def welcome(request,name):
    return HttpResponse(f"Hello {name}")


def ListExpidation(request):
    liste = expedition.objects.filter(status='p').order_by('-created_at')
    return render(request, "expidation/list.html",{"list":liste})

def detailExpidation(request,reference):
    details = expedition.objects.get(reference=reference)
    return render(request, "expidation/detail.html",{"detail":details})


def deleteExpidation(request,reference):
    choix = expedition.objects.get(reference=reference)
    choix.delete()
    return render(request,"expidation/delete.html",{"choix":choix})