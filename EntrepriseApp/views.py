from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from EntrepriseApp.models import Utilisatuer
from .forms import ProfileForm, registeruserform
# Create your views here.
def register(request):
    if request.method =="POST":
        form = registeruserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')    
    else:
        form = registeruserform()

    return render(request, 'register.html', {'form': form})

class ModifierProfile(LoginRequiredMixin, UpdateView):
    model = Utilisatuer
    template_name = "profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('Expidation:listview')

    def get_object(self, queryset=None):
        return self.request.user


class SupprimerProfile(LoginRequiredMixin, DeleteView):
    model = Utilisatuer
    template_name = "profile_delete.html"
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user