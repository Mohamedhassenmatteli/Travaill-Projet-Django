from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.
class vehicules(models.Model):
    immatriculation = models.CharField(max_length=20,unique=True)
    capacite_kg = models.PositiveIntegerField(validators=[
        MinValueValidator(1,"La capacite ne peut pas etre negative"),
    ])
    entreprise = models.ForeignKey('EntrepriseApp.Enterprise',on_delete=models.CASCADE,related_name='vehicules')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    disponible = models.BooleanField(default=True)
    type_vehicule = models.CharField(max_length=20,choices=[])
    def clean(self):
        if self.entreprise_id and self.entreprise.type_entreprise != 'transporteur':
            raise ValidationError(({
                'entreprise : un vehicule ne peut etre cree que par un transporteur'
            }))