from django.contrib import admin
from Usuario.models import Usuario
from django.contrib.auth.models import Permission


class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'nombres',
        'apellidos',
        'is_active',
        'is_staff',
        'is_superuser',

    )
    search_fields=['id_usuario']


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Permission)