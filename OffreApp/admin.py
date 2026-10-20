import csv

from django.contrib import admin
from django.utils.html import format_html 
from .models import offre   
from django.http import HttpResponse 
# Register your models here.
class admin_offre(admin.ModelAdmin):
    search_fields = ('expedition', 'transporteur', 'vehicule') 
class FilterBYPrice(admin.SimpleListFilter): 
      title = "prix"
      parameter_name = "prix"
      def lookups(self,request,model_admin):
          return  [('low','<1000'),('medium','1000-10000'),('high','>10000')]
      def queryset(self,request,queryset):
          if self.value() == 'low':
              return queryset.filter(prix__lt=1000)
          if self.value() == 'medium':
              return queryset.filter(prix__gte=1000, prix__lte=10000)
          if self.value() == 'high':
              return queryset.filter(prix__gt=10000)
          return queryset

@admin.register(offre)
class offre_admin(admin.ModelAdmin):
    list_display = ('prix','delais_jour','status','date_proposition','expedition','transporteur','vehicule')
    autocomplete_fields = ('expedition', 'transporteur', 'vehicule') 
    list_filter = ('status', 'date_proposition', 'prix',FilterBYPrice)
    readonly_fields = ('date_proposition', 'created_at', 'updated_at') 
    fieldsets = ( 
        ('Détails de l\'offre', {'fields': ('expedition', 'transporteur', 'vehicule')}), 
        ('prix', {'fields': ('prix',)}), 
        ('Suivi', {'fields': ('date_proposition', 'created_at', 
        'updated_at')}), 
    ) 
    def get_readonly_fields(self, request, obj=None): 
        base = list(self.readonly_fields) 
        if obj and obj.statut == 'acceptee': 
            return base + ['prix', 'delai_jours'] 
        return base
@admin.display(description='Statut') 
def statut_colore(self, obj): 
    couleurs = { 
        'proposee': '#F0AD4E', 'acceptee': '#5CB85C', 
        'refusee': '#D9534F', 'retiree': '#777777', 
    } 
    return format_html( 
        '<span style="color:white;background:{};padding:3px 8px; border-radius:4px;">{}</span>', 
        couleurs.get(obj.statut, '#999'), obj.get_statut_display(), 
    ) 
@admin.action(description="Exporter la sélection en CSV") 
def exporter_offres_csv(modeladmin, request, queryset): 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment; filename="offres.csv"' 
    writer = csv.writer(response) 
    writer.writerow(['reference_expedition', 'transporteur', 'prix', 'statut']) 
    for offre in queryset.select_related('expedition', 'transporteur'): 
        writer.writerow([offre.expedition.reference, offre.transporteur.raison_sociale, 
        offre.prix, offre.statut]) 
    return response 