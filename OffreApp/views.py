from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from OffreApp.form import OffreForm
from .models import offre
from django.urls import reverse_lazy
# Create your views here.
class ListOffre(ListView):
    model = offre
    template_name = "offre/list.html"
    context_object_name = 'list'
class DetailOffre(DetailView):
    model = offre
    template_name = "offre/detail.html"
    context_object_name = 'detail'
class CreateOffre(CreateView):
    model = offre
    template_name = "offre/forms.html"
    form_class = OffreForm
    success_url = reverse_lazy('Offre:listview')
class UpdateOffre(UpdateView):
    model = offre
    template_name= "offre/forms.html"
    form_class = OffreForm
    success_url = reverse_lazy('Offre:listview')
class deleteOffre(DeleteView):
    model = offre
    template_name = "offre/delete.html"
    success_url = reverse_lazy('Offre:listview')
    
