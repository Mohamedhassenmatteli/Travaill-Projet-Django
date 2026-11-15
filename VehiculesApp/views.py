from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import VehiculeForm
from .models import vehicules


class Liste_vehicules(ListView):
    model = vehicules
    template_name = "vehicule/list.html"
    context_object_name = "list"


class Detail_vehicule(DetailView):
    model = vehicules
    template_name = "vehicule/detail.html"
    context_object_name = "detail"


class Ajouter_vehicule(CreateView):
    model = vehicules
    form_class = VehiculeForm
    template_name = "vehicule/forms.html"
    success_url = reverse_lazy("Vehicules:listview")


class Modifier_vehicule(UpdateView):
    model = vehicules
    form_class = VehiculeForm
    template_name = "vehicule/forms.html"
    success_url = reverse_lazy("Vehicules:listview")


class Supprimer_vehicule(DeleteView):
    model = vehicules
    template_name = "vehicule/delete.html"
    success_url = reverse_lazy("Vehicules:listview")
