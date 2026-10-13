from django.contrib import admin

from .models import expedition

@admin.register(admin.ModelAdmin)
class expedition_admin(admin.ModelAdmin):
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
