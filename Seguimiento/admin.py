from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import DetalleBalance, Fase
from .models import Periodo, Partida, Balance, Proyecto


#  PERMISOS PERSONALIZADOS


class FaseFilter(SimpleListFilter):
    title = 'Fase'
    parameter_name = 'fase'

    def lookups(self, request, model_admin):
        """
        Opciones que aparecerán en el filtro.
        """
        fases = Fase.objects.all()
        return [(fase.id, str(fase)) for fase in fases]

    def queryset(self, request, queryset):
        """
        Filtrar el queryset de DetalleBalance según la fase seleccionada.
        """
        if self.value():
            return queryset.filter(balance__fase__id=self.value())
        return queryset


class PartidaFilter(SimpleListFilter):
    title = 'Partida'
    parameter_name = 'partida'

    def lookups(self, request, model_admin):
        """
        Opciones que aparecerán en el filtro.
        """
        # Verificar si hay un filtro de fase activo
        fase_id = request.GET.get('fase')
        if fase_id:
            partidas = Partida.objects.filter(balance__fase__id=fase_id).distinct()
        else:
            partidas = Partida.objects.all()

        return [(partida.id, str(partida)) for partida in partidas]

    def queryset(self, request, queryset):
        """
        Filtrar el queryset de DetalleBalance según la partida seleccionada.
        """
        if self.value():
            return queryset.filter(balance__partida__id=self.value())
        return queryset


# Acción para actualizar registros
@admin.action(description='Actualizar registros')
def actualizar_registros(queryset):
    # Calcular Plan acumulado
    acumulado_plan = 0
    for detalle in queryset.order_by('id'):
        acumulado_plan += detalle.planificado
        detalle.plan_acumulado = acumulado_plan
        detalle.save()
        if acumulado_plan == 120:
            break
    print("Se ha ejecutado 1 Acción: Calcular Plan acumulado")

    # Calcular realizado acumulado
    acumulado_real = 0
    for detalle in queryset.order_by('periodo'):
        if detalle.realizado is None:
            break
        elif acumulado_real == 120:
            break
        elif detalle.realizado is None:
            acumulado_real += 0
        else:
            acumulado_real += detalle.realizado
        # detalle.realizado = acumulado_real
        detalle.save()
    print("Se ha ejecutado 1 Acción: Calcular realizado acumulado")

    # Calcular la proyección Media
    acumulado_pm = 0
    contador_pm = 0
    for detalle in queryset.order_by('periodo'):
        if detalle.realizado is None:
            detalle.proyeccion_media = 0
            detalle.save()

        else:
            acumulado_pm += detalle.realizado
            contador_pm += 1
            # print("acumulado ", acumulado_pm)
            # print("contador ", contador_pm)
            detalle.proyeccion_media = acumulado_pm // contador_pm  # División entera para resultado aproximado
            detalle.save()
    print("Se ha ejecutado 1 Acción: Calcular la proyección Media")

    # Calcular la proyección media acumulada
    acumulado_proyeccion = 0
    for detalle in queryset.order_by('periodo'):
        acumulado_proyeccion += detalle.proyeccion_media
        detalle.proyeccion_acumulado_media = acumulado_proyeccion
        detalle.save()

    print("Se ha ejecutado 1 Acción: Calcular la proyección media acumulada")

    # Calcular la proyección empirica acumulada

    acumulado_proyeccion_e = 0
    id_lst_ra = queryset.order_by('realizado_acumulado').values_list('realizado_acumulado', flat=True).distinct()
    # print(id_lst_ra)
    id_lst_ra = list(id_lst_ra)
    # print(id_lst_ra)
    id_lst_ra.remove(None)
    # print(id_lst_ra)
    id_lst_ra.sort(reverse=True)
    valor = id_lst_ra[0]
    # print(valor)
    reg = len(id_lst_ra)
    # print("largo", reg)

    x = 1
    for registro in queryset.order_by('periodo'):
        if x >= reg:
            if x == reg:
                registro.proyeccion_empirica_acumulada = valor
                acumulado_proyeccion_e += valor
                registro.save()
            else:
                if registro.proyeccion_empirica is None:
                    acumulado_proyeccion_e += 0
                    registro.proyeccion_empirica_acumulada = acumulado_proyeccion_e
                    registro.save()
                else:
                    acumulado_proyeccion_e += registro.proyeccion_empirica
                    registro.proyeccion_empirica_acumulada = acumulado_proyeccion_e
                    registro.save()
        x = x + 1

    for registro in queryset.order_by('periodo'):
        if registro.proyeccion_empirica_acumulada is None:
            registro.proyeccion_empirica_acumulada = None
            registro.save()
        elif registro.proyeccion_empirica_acumulada < valor:
            registro.proyeccion_empirica_acumulada = None
            registro.save()
        elif registro.proyeccion_empirica_acumulada > 125:
            registro.proyeccion_empirica_acumulada = None
            registro.save()

    print("Se ha ejecutado 1 Acción: Calcular la proyección empirica acumulada")


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
        fields = ('id', 'partida', 'fase')
        export_order = ('id', 'partida', 'fase')


class DetalleBalanceResource(resources.ModelResource):
    class Meta:
        model = DetalleBalance
        fields = ('id', 'balance', 'en_plan', 'periodo', 'semana_trabajo', 'planificado', 'realizado', 'plan_acumulado',
                  'realizado_acumulado', 'proyeccion_media', 'proyeccion_acumulado_media', 'proyeccion_empirica',
                  'proyeccion_empirica_acumulada')
        export_order = (
        'id', 'balance', 'en_plan', 'periodo', 'semana_trabajo', 'planificado', 'realizado', 'plan_acumulado',
        'realizado_acumulado', 'proyeccion_media', 'proyeccion_acumulado_media', 'proyeccion_empirica',
        'proyeccion_empirica_acumulada')


# Define el inline para DetalleBalance
class DetalleBalanceInline(admin.TabularInline):
    model = DetalleBalance
    extra = 1  # Número de filas vacías al agregar nuevos objetos
    min_num = 1  # Número mínimo de objetos requeridos
    fields = (
    'periodo', 'semana_trabajo', 'en_plan', 'planificado', 'realizado', 'proyeccion_empirica', 'proyeccion_media',
    'plan_acumulado','realizado_acumulado','proyeccion_empirica_acumulada',  'proyeccion_acumulado_media')
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
    list_display = ('id', 'fase', 'partida')
    list_filter = ('fase', 'partida')
    search_fields = ('partida__nombre',)
    ordering = ('id',)
    inlines = [DetalleBalanceInline]  # Agregar el inline para DetalleBalance


# Admin de DetalleBalance no es necesario ya que ahora está en línea en Balance
@admin.register(DetalleBalance)
class DetalleBalanceAdmin(ImportExportModelAdmin):
    # form = DetalleBalanceForm
    resource_class = DetalleBalanceResource
    list_display = (
    'id', 'balance', 'periodo', 'semana_trabajo', 'en_plan', 'planificado', 'realizado', 'proyeccion_empirica', 'proyeccion_media',
    'plan_acumulado','realizado_acumulado','proyeccion_empirica_acumulada','proyeccion_acumulado_media')
    search_fields = ('balance__id', 'periodo__semana')
    # list_filter = ('en_plan','balance__fase__Proyecto', 'balance__fase__nombre_fase' , 'balance__partida__nombre')
    list_filter = [FaseFilter, PartidaFilter]
    ordering = ('periodo',)
    actions = [actualizar_registros]
    """formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size': 1})},
    }"""


class Media:


    css = {
        'all': ('admin/css/custom_admin.css',)  # Ruta al archivo CSS personalizado
    }


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    pass


@admin.register(Fase)
class FaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'Proyecto', 'nombre_fase', 'is_active',)
    list_filter = ('id', 'Proyecto', 'nombre_fase', 'is_active',)