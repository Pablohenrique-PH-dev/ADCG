from django.contrib import admin
from .models import Estudo, Episodio, Usuario # Filme
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('estudos_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Estudo) # Filme
admin.site.register(Episodio) # Filme
admin.site.register(Usuario, UserAdmin)