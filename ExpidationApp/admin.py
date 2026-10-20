from django.contrib import admin

from .models import expedition
from django.utils import timezone 
 
class EnRetardFilter(admin.SimpleListFilter): 
    title = 'en retard' 
    parameter_name = 'en_retard' 
 
    def lookups(self, request, model_admin): 
        return [('oui', 'Oui'), ('non', 'Non')] 
 
    def queryset(self, request, queryset): 
        aujourd_hui = timezone.now().date()
        if self.value() == 'oui': 
            return queryset.filter(status='publiee', 
date_souhaitee__lt = aujourd_hui)
        if self.value() == 'non': 
            return queryset.exclude(status='publiee', 
date_souhaitee__lt=aujourd_hui) 
        return queryset 

@admin.register(expedition)
class expedition_admin(admin.ModelAdmin):
    list_filter = ('status', 'ville_depart', EnRetardFilter)
    list_display = ('ville_depart','ville_arrivee','status')
    readonly_fields = ('created_at','updated_at')
    search_fields = ('ville_depart', 'ville_arrivee')
    fieldsets = (
        ('Détails de l\'expédition', {
            'fields': ('ville_depart', 'ville_arrivee', 'status','date_souhaitee','entreprise','description','poids_kg')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
