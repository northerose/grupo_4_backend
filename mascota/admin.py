from django.contrib import admin
from mascota.models import Mascota

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'responsable']

admin.site.register(Mascota, MascotaAdmin)