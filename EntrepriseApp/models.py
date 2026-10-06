from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator , RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.


# Validators
def validate_email(value):
    if not value:
        raise ValidationError("L'email ne peut pas etre vide")
    if not value.endswith('@gmail.com'):
        raise ValidationError("Le domaine accepté est gmail")

matricule_fiscale = RegexValidator(
    regex = "^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$ ",
    message = "Format erroné"
)
    
class Utilisatuer(AbstractUser):
    user_id = models.CharField(primary_key=True,max_length=8)
    email = models.EmailField(unique=True,validators=[validate_email])
    telephone = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=20,choices=[
        ('admin','Admin'),
        ('c','Chargeur'),
        ('t','Transporteur')
    ],default='c')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


class Enterprise(models.Model):
    raison_social = models.CharField(max_length=200,blank=False,null=False)
    matricule_fiscale = models.CharField(max_length=17,unique=True)
    adress = models.TextField(validators=[
        MinLengthValidator(20,"L'adresse ne peut pas avoir mois de 20 char")
    ,   MaxLengthValidator(400,"L'adresse ne peut pas avoir plus de 400 char")]
    )
    type_entreprise = models.CharField(max_length=100,choices=[
        ('c','Chargeur'),
        ('t','Transporteur')
    ])

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    gerant = models.OneToOneField(Utilisatuer,on_delete=models.CASCADE,related_name='entreprise')


