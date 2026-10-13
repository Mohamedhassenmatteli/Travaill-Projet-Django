from django.contrib import admin
from .models import offre   
# Register your models here.
@admin.register(offre)
class offre_admin(admin.ModelAdmin):
    list_display = ('prix','delais_jour','status','date_proposition','expedition','transporteur','vehicule')
    readonly_fields = ('created_at','updated_at')
    fieldsets = (
        ('Détails de l\'offre', {
            'fields': ('prix', 'delais_jour', 'status')
        }),
        ('Informations sur l\'expédition et le transporteur', {
            'fields': ('expedition', 'transporteur', 'vehicule')
        }),
        ('Horodatage', {
            'fields': ( 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )