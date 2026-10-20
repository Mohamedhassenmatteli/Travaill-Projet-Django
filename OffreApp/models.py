from django.db import models, transaction
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from ExpidationApp.models import expedition
# Create your models here.
class offre(models.Model):
    prix = models.FloatField(validators=[MinValueValidator(1,"Le prix ne peut pas etre negative")])
    delais_jour = models.IntegerField(blank=False,null=False,validators=[MinValueValidator(1,"Le delais ne peut pas etre negative")])
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
    def clean(self):
        super().clean()
        if self.transporteur_id and self.transporteur.type_entreprise != 't':
            raise ValidationError({
                'transporteur': (
                    'Une offre ne peut être faite que par un transporteur.'
                )
            })
        if (
            self.vehicule_id
            and self.transporteur_id
            and self.vehicule.entreprise_id != self.transporteur_id
        ):
            raise ValidationError({
                'vehicule': (
                    "Le véhicule associé à une offre doit appartenir à la "
                    "même entreprise que le transporteur de l'offre."
                )
            })
        if self.expedition_id and self.expedition.status != "p":
            raise ValidationError({
                'expedition': (
                    "Une expédition ne peut recevoir de nouvelles offres "
                    "que si son statut est publiée."
                )
            })
        if self.transporteur_id and self.expedition_id and self.status == "p":
            offres_existantes = offre.objects.filter(
                transporteur_id=self.transporteur_id,
                expedition_id=self.expedition_id,
                status="p",
            )
            if self.pk:
                offres_existantes = offres_existantes.exclude(
                    pk=self.pk
                )
            if offres_existantes.exists():
                raise ValidationError({
                    'transporteur': (
                        "Cette entreprise possède déjà une offre proposée "
                        "pour cette expédition."
                    )
                })
        if self.vehicule_id and self.status == 'p' and not self.vehicule.disponible:
            raise ValidationError({
                'vehicule': (
                    "Ce véhicule n'est pas disponible pour une nouvelle offre."
                )
            })

        
    def save(self, *args, **kwargs):
        with transaction.atomic():
            ancienne_offre = None

            if self.pk:
                ancienne_offre = (
                    offre.objects
                    .select_for_update()
                    .filter(pk=self.pk)
                    .first()
                )

            devient_acceptee = (
                self.status == 'a'
                and (
                    ancienne_offre is None
                    or ancienne_offre.status != 'a'
                )
            )

            self.full_clean()
            super().save(*args, **kwargs)

            if devient_acceptee:
                expedition.objects.filter(
                    pk=self.expedition_id
                ).update(status='a')

                offre.objects.filter(
                    expedition_id=self.expedition_id,
                    status='p'
                ).exclude(
                    pk=self.pk
                ).update(status='r')

    