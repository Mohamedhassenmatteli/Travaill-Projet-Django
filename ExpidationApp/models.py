from django.db import models
from django.core.validators import     MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class expedition(models.Model):
    entreprise = models.ForeignKey('EntrepriseApp.Enterprise',on_delete=models.CASCADE,related_name='expeditions')
    reference = models.CharField(max_length=20, unique=True, editable=False)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_kg = models.FloatField(validators=[
        MinValueValidator(1,"Le poids ne peut pas etre negative")
    ])
    date_souhaitee = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=20,choices=[
        ('p','publiee'),
        ('a','attribuee'),
        ('ec','en_cours'),
        ('l','livree'),
        ('an','annulee')
    ],default='p')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'c':
            raise ValidationError({
                'entreprise': (
                    'Une expédition ne peut être créée que par un chargeur.'
                )
            })
    @classmethod
    def _generate_reference(cls):
        prefix = f"EXP_{timezone.now():%y}"
        dernier = (
            cls.objects.filter(reference__startswith=prefix)
            .order_by("-reference")
            .first()
        )
        compteur = int(dernier.reference[-5:]) + 1 if dernier else 1
        if compteur > 99999:
            raise ValueError("La limite de références d'expédition est atteinte.")
        return f"{prefix}{compteur:05d}"

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        self.full_clean()
        super().save(*args,**kwargs)
