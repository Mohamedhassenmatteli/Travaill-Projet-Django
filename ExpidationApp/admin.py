from django.contrib import admin

from .models import expedition
from django.utils import timezone 
 
class EnRetardFilter(admin.SimpleListFilter): 
    title = 'en retard' 
    parameter_name = 'en_retard' 
 
    def lookups(self, request, model_admin): 
        return [('oui', 'Oui'), ('non', 'Non')] 
 
    def queryset(self, request, queryset): 
        if self.value() == 'oui': 
            return queryset.filter(statut='publiee', 
date_souhaitee__lt=timezone.now().date()) 
        if self.value() == 'non': 
            return queryset.exclude(statut='publiee', 
date_souhaitee__lt=timezone.now().date()) 
        return queryset 

@admin.register(admin.ModelAdmin)
class expedition_admin(admin.ModelAdmin):
    list_filter = ('statut', 'ville_depart', EnRetardFilter)
    list_display = ('expedition_id','ville_depart','ville_arrivee','status')
    readonly_fields = ('created_at','updated_at')
    fieldsets = (
        ('Détails de l\'expédition', {
            'fields': ('expedition_id', 'ville_depart', 'ville_arrivee', 'status')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
