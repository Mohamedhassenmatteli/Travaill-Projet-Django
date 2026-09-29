from django.db import models

# Create your models here.
class offre(models.Model):
    prix = models.FloatField()
    delais_jour = models.IntegerField(blank=False,null=False)
    status = models.CharField(max_length=20,choices=[
        ('p','proposee'), 
        ('a','acceptee'),
        ('r','refusee'),
        ('re','retiree'),
        
    ],default='p')
    date_proposition = models.DateTimeField(auto_now_add=True)
    expedition = models.ForeignKey('ExpidationApp.expedition',on_delete=models.CASCADE,related_name='offres')
    transporteur = models.ForeignKey('EntrepriseApp.Enterprise',on_delete=models.CASCADE,related_name='offres')
    vehicule = models.ForeignKey('VehiculesApp.vehicules',on_delete=models.CASCADE,related_name='offres')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    