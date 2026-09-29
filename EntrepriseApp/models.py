from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Utilisatuer(AbstractUser):
    user_id = models.CharField(primary_key=True,max_length=8)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=20,choices=[
        ('admin','Admin'),
        ('c','Chargeur'),
        ('t','Transporteur')
    ],default='c')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    gerant = models.OneToOneField(Utilisatuer,on_delete=models.CASCADE,related_name='entreprise')


class Enterprise(models.Model):
    raison_social = models.CharField(max_length=200,blank=False,null=False)
    matricule_fiscale = models.CharField(max_length=17,unique=True)
    adress = models.TextField()
    type_entreprise = models.CharField(max_length=100,choices=[
        ('c','Chargeur'),
        ('t','Transporteur')
    ])

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


