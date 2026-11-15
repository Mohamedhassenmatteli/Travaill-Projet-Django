from django import forms

from .models import vehicules


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = vehicules
        exclude = ["created_at", "updated_at"]
