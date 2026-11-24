from django import forms
from django.http import HttpResponse
from django.urls import reverse_lazy

from ExpidationApp.forms import ExpeditionForm
from .models import expedition
from django.shortcuts import  render 
from django.views.generic import DetailView, ListView , DeleteView , CreateView, UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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


@login_required
def deleteExpidation(request,reference):
    choix = expedition.objects.get(reference=reference)
    choix.delete()
    return render(request,"expidation/delete.html",{"choix":choix})

class Liste_expidation(ListView):
    model = expedition
    template_name = "expidation/list.html"  
    context_object_name = 'list'

class detail_expidation(DetailView):
    model= expedition
    template_name = "expidation/detail.html"
    context_object_name = 'detail'

class delete_expidation(LoginRequiredMixin, DeleteView):
    model = expedition
    template_name = "expidation/delete.html"
    success_url = reverse_lazy('Expidation:listview')

class Ajouter_Expedition(CreateView):
        model = expedition
        template_name = "expidation/forms.html"
        # fields = "__all__"
        form_class = ExpeditionForm
        success_url = reverse_lazy('Expidation:listview')

class Update_Expedition(LoginRequiredMixin,UpdateView):
        model = expedition
        template_name = "expidation/forms.html"
        # fields = "__all__"
        form_class = ExpeditionForm
        success_url = reverse_lazy('Expidation:listview')