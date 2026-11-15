from django.forms import ModelForm
from django import forms
from .models import offre
class OffreForm(ModelForm):
    class Meta:
        model = offre
        fields = '__all__'
        exclude = ['id', 'created_at', 'updated_at']
        widgets = {
            "data_date_proposition" : forms.DateTimeInput(attrs={'type': 'datetime-local'},),
        }
        