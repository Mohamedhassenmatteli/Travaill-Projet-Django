from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin
from OffreApp.models import offre
from VehiculesApp.models import vehicules
from .models  import Enterprise,Utilisatuer
# Register your models here.
admin.site.site_header = "Transconnect- Administration"
admin.site.site_title = "Transconnect"
admin.site.index_title = "Tableau de bord"
class VehiculeInline(admin.TabularInline): 
    model = vehicules 
    extra = 0 
    fields = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible') 
    show_change_link = True
class OffreInline(admin.StackedInline): 
    model = offre 
    extra = 0 
    fk_name = 'expedition' 
    readonly_fields = ('transporteur', 'vehicule', 'prix', 'delai_jours', 'statut') 
    show_change_link = True 
    can_delete = False 
class UtilisateurAdmin(UserAdmin):
    list_display = ('user_id','username','email','is_active','is_superuser','role')
    list_editable = ('username','is_active',)
    search_fields = ('raison_sociale', 'matricule_fiscal')
    fieldsets = (
    
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('email', 'telephone', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_filter = ('is_active','role')
    list_display = (
            "user_id",
            "username",
            "role",
            "email",
            "telephone",
            "is_active",
        )
    add_fieldsets = (
            
           ( None,
            {
                "classes": ("wide",),
                "fields" : (
                    "username",
                    "usable_password",
                    "password1",
                    "password2",
                    "email",
                    "telephone",
                    "role",
                ),
            },
          ),
        )   
    list_per_page = 1
class EntrepriseAdmin(admin.ModelAdmin): 
    search_fields = ('raison_sociale', 'matricule_fiscal') 
    inlines = [VehiculeInline]


admin.site.register(Utilisatuer,UtilisateurAdmin) 
admin.site.register(Enterprise,EntrepriseAdmin)