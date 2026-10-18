from django.contrib import admin

from OffreApp.models import offre
from VehiculesApp.models import vehicules
from .models  import Enterprise,Utilisatuer
# Register your models here.
class VehiculeInline(admin.TabularInline): 
    model = vehicules 
    extra = 0 
    fields = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible') 
class OffreInline(admin.StackedInline): 
    model = offre 
    extra = 0 
    fk_name = 'expedition' 
    readonly_fields = ('transporteur', 'vehicule', 'prix', 'delai_jours', 'statut') 
    show_change_link = True 
    can_delete = False 
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','username','email','is_active','is_superuser','role')
    list_editable = ('username','is_active',)
    search_fields = ('raison_sociale', 'matricule_fiscal') 
    list_filter = ('is_active','role')
    list_per_page = 1
admin.site.register(Utilisatuer,UserAdmin) 
admin.site.register(Enterprise)
class EntrepriseAdmin(admin.ModelAdmin): 
    search_fields = ('raison_sociale', 'matricule_fiscal') 
    inlines = [VehiculeInline]
