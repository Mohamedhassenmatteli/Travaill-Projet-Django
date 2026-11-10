from django import forms
from .models import expedition
class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = expedition
        fields = '__all__'
        exclude = ['reference', 'id', 'created_at', 'updated_at',"id"]
        widgets = {
                    'date_souhaitee': forms.DateTimeInput(attrs={'type': 'datetime-local'},),
                }