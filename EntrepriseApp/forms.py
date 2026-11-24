from django import forms
from django.contrib.auth.forms import UserCreationForm

from EntrepriseApp.models import Utilisatuer


class registeruserform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilisatuer
        fields = UserCreationForm.Meta.fields + ('email','telephone','role')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Utilisatuer
        fields = ("username", "email", "telephone", "role")