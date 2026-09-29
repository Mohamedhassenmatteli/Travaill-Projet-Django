from django.db import models

# Create your models here.
class expedition(models.Model):
    entreprise = models.ForeignKey('EntrepriseApp.Enterprise',on_delete=models.CASCADE,related_name='expeditions')
    reference = models.CharField(max_length=20,unique=True,auto_created=True)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_kg = models.FloatField()
    date_souhaitee = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=20,choices=[
        ('p','publiee'),
        ('a','attribuee'),
        ('ec','en_cours'),
        ('l','livree'),
        ('an','annulee')
    ],default='publiee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)