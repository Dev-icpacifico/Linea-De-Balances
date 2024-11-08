from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Periodo, Partida, Balance, DetalleBalance, Proyecto, Fase



# Acción para rellenar plan_acumulado
@admin.action(description='Calcular Plan Acumulado')
def rellenar_plan_acumulado(modeladmin, request, queryset):
    acumulado = 0
    for detalle in queryset.order_by('id'):
        acumulado += detalle.planificado
        detalle.plan_acumulado = acumulado
        detalle.save()

# Acción para rellenar realizado_acumulado
@admin.action(description='Calcular Realizado Acumulado')
def rellenar_realizado_acumulado(modeladmin, request, queryset):
    acumulado = 0
    for detalle in queryset.order_by('id'):
        acumulado += detalle.realizado
        detalle.realizado_acumulado = acumulado
        detalle.save()

# Acción para calcular la proyección media
@admin.action(description='Calcular Proyección Media')
def calcular_proyeccion_media(modeladmin, request, queryset):
    acumulado = 0
    contador = 0
    for detalle in queryset.order_by('id'):
        acumulado += detalle.realizado
        contador += 1
        print("acumulado ", acumulado)
        print("contador ", contador)
        detalle.proyeccion_media = acumulado // contador  # División entera para resultado aproximado
        detalle.save()


# Acción para calcular la proyección acumulada de proyección_media
@admin.action(description='Calcular Proyección Acumulada')
def calcular_proyeccion_acumulado_media(modeladmin, request, queryset):
    acumulado_proyeccion = 0
    for detalle in queryset.order_by('id'):
        acumulado_proyeccion += detalle.proyeccion_media
        detalle.proyeccion_acumulado_media = acumulado_proyeccion
        detalle.save()
"""class DetalleBalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance', 'en_plan', 'periodo', 'planificado', 'plan_acumulado', 'realizado')"""



# Define los recursos de importación/exportación
class PeriodoResource(resources.ModelResource):
    class Meta:
        model = Periodo
        fields = ('id', 'semana', 'fecha')
        export_order = ('id', 'semana', 'fecha')

class PartidaResource(resources.ModelResource):
    class Meta:
        model = Partida
        fields = ('id', 'nombre')
        export_order = ('id', 'nombre')

class BalanceResource(resources.ModelResource):
    class Meta:
        model = Balance
        fields = ('id', 'partida')
        export_order = ('id', 'partida')

class DetalleBalanceResource(resources.ModelResource):
    class Meta:
        model = DetalleBalance
        fields = ('id', 'balance', 'en_plan', 'periodo','semana_trabajo','planificado', 'realizado', 'plan_acumulado', 'realizado_acumulado', 'proyeccion_media', 'proyeccion_acumulado_media', 'proyeccion_empirica', 'proyeccion_empirica_acumulada')
        export_order = ('id', 'balance', 'en_plan', 'periodo','semana_trabajo','planificado', 'realizado', 'plan_acumulado', 'realizado_acumulado', 'proyeccion_media', 'proyeccion_acumulado_media', 'proyeccion_empirica', 'proyeccion_empirica_acumulada')

# Define el inline para DetalleBalance
class DetalleBalanceInline(admin.TabularInline):
    model = DetalleBalance
    extra = 1  # Número de filas vacías al agregar nuevos objetos
    min_num = 1  # Número mínimo de objetos requeridos
    fields = ('periodo','semana_trabajo', 'en_plan', 'planificado', 'realizado', 'plan_acumulado', 'realizado_acumulado', 'proyeccion_media', 'proyeccion_acumulado_media', 'proyeccion_empirica', 'proyeccion_empirica_acumulada')
    show_change_link = True

# Registra los modelos en el administrador
@admin.register(Periodo)
class PeriodoAdmin(ImportExportModelAdmin):
    resource_class = PeriodoResource
    list_display = ('id', 'semana', 'fecha')
    search_fields = ('semana', 'fecha')
    list_filter = ('semana', 'fecha')
    ordering = ('semana', 'fecha')

@admin.register(Partida)
class PartidaAdmin(ImportExportModelAdmin):
    resource_class = PartidaResource
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Balance)
class BalanceAdmin(ImportExportModelAdmin):
    resource_class = BalanceResource
    list_display = ('id','fase', 'partida')
    search_fields = ('partida__nombre',)
    ordering = ('id',)
    actions = [rellenar_plan_acumulado]
    inlines = [DetalleBalanceInline]  # Agregar el inline para DetalleBalance

# Admin de DetalleBalance no es necesario ya que ahora está en línea en Balance
@admin.register(DetalleBalance)
class DetalleBalanceAdmin(ImportExportModelAdmin):
    resource_class = DetalleBalanceResource
    list_display = ('id', 'balance', 'periodo','semana_trabajo','en_plan', 'planificado', 'realizado', 'plan_acumulado', 'realizado_acumulado', 'proyeccion_media', 'proyeccion_acumulado_media', 'proyeccion_empirica', 'proyeccion_empirica_acumulada')
    search_fields = ('balance__id', 'periodo__semana')
    list_filter = ('en_plan', 'periodo__semana','balance' )
    ordering = ('id',)
    actions = [rellenar_plan_acumulado, rellenar_realizado_acumulado, calcular_proyeccion_media, calcular_proyeccion_acumulado_media]

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    pass

@admin.register(Fase)
class FaseAdmin(admin.ModelAdmin):
    pass