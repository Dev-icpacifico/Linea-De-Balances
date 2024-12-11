from django.contrib.admin import site
from django.views.generic import TemplateView
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import (
    ProyectoSerializer,
    FaseSerializer,
    PeriodoSerializer,
    PartidaSerializer,
    BalanceSerializer,
    DetalleBalanceSerializer,
)


class Report(TemplateView):
    template_name = 'admin/reportbi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega el contexto del admin
        context.update(site.each_context(self.request))
        context['title'] = 'Reportes BI'  # Título personalizado
        return context


@extend_schema_view(
    list=extend_schema(
        description="Obtiene una lista de todos los proyectos registrados.",
        summary="Lista de Proyectos",
        tags=["Proyecto"]
    ),
    retrieve=extend_schema(
        description="Obtiene los detalles de un proyecto específico por su ID.",
        summary="Detalle de Proyecto",
        tags=["Proyecto"]
    ),
    create=extend_schema(
        description="Crea un nuevo proyecto con los datos proporcionados.",
        summary="Crear Proyecto",
        tags=["Proyecto"]
    ),
    update=extend_schema(
        description="Actualiza todos los campos de un proyecto existente.",
        summary="Actualizar Proyecto",
        tags=["Proyecto"]
    ),
    partial_update=extend_schema(
        description="Actualiza parcialmente los campos de un proyecto.",
        summary="Actualizar Parcialmente Proyecto",
        tags=["Proyecto"]
    ),
    destroy=extend_schema(
        description="Elimina un proyecto existente por su ID.",
        summary="Eliminar Proyecto",
        tags=["Proyecto"]
    ),
)
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    list=extend_schema(
        description="Obtiene una lista de todas las fases disponibles.",
        summary="Lista de Fases",
        tags=["Fase"]
    ),
    retrieve=extend_schema(
        description="Obtiene los detalles de una fase específica por su ID.",
        summary="Detalle de Fase",
        tags=["Fase"]
    ),
    create=extend_schema(
        description="Crea una nueva fase con los datos proporcionados.",
        summary="Crear Fase",
        tags=["Fase"]
    ),
    update=extend_schema(
        description="Actualiza todos los campos de una fase existente.",
        summary="Actualizar Fase",
        tags=["Fase"]
    ),
    partial_update=extend_schema(
        description="Actualiza parcialmente los campos de una fase existente.",
        summary="Actualizar Parcialmente Fase",
        tags=["Fase"]
    ),
    destroy=extend_schema(
        description="Elimina una fase específica por su ID.",
        summary="Eliminar Fase",
        tags=["Fase"]
    ),
)

class FaseViewSet(viewsets.ModelViewSet):
    queryset = Fase.objects.all()
    serializer_class = FaseSerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    list=extend_schema(
        description="Obtiene una lista de todos los periodos registrados.",
        summary="Lista de Periodos",
        tags=["Periodo"]
    ),
    retrieve=extend_schema(
        description="Obtiene los detalles de un periodo específico por su ID.",
        summary="Detalle de Periodo",
        tags=["Periodo"]
    ),
    create=extend_schema(
        description="Crea un nuevo periodo con los datos proporcionados.",
        summary="Crear Periodo",
        tags=["Periodo"]
    ),
    update=extend_schema(
        description="Actualiza todos los campos de un periodo existente.",
        summary="Actualizar Periodo",
        tags=["Periodo"]
    ),
    partial_update=extend_schema(
        description="Actualiza parcialmente los campos de un periodo existente.",
        summary="Actualizar Parcialmente Periodo",
        tags=["Periodo"]
    ),
    destroy=extend_schema(
        description="Elimina un periodo específico por su ID.",
        summary="Eliminar Periodo",
        tags=["Periodo"]
    ),
)

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    list=extend_schema(
        description="Obtiene una lista de todas las partidas registradas.",
        summary="Lista de Partidas",
        tags=["Partida"]
    ),
    retrieve=extend_schema(
        description="Obtiene los detalles de una partida específica por su ID.",
        summary="Detalle de Partida",
        tags=["Partida"]
    ),
    create=extend_schema(
        description="Crea una nueva partida con los datos proporcionados.",
        summary="Crear Partida",
        tags=["Partida"]
    ),
    update=extend_schema(
        description="Actualiza todos los campos de una partida existente.",
        summary="Actualizar Partida",
        tags=["Partida"]
    ),
    partial_update=extend_schema(
        description="Actualiza parcialmente los campos de una partida existente.",
        summary="Actualizar Parcialmente Partida",
        tags=["Partida"]
    ),
    destroy=extend_schema(
        description="Elimina una partida específica por su ID.",
        summary="Eliminar Partida",
        tags=["Partida"]
    ),
)

class PartidaViewSet(viewsets.ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    list=extend_schema(
        description="Obtiene una lista de todos los balances registrados.",
        summary="Lista de Balances",
        tags=["Balance"]
    ),
    retrieve=extend_schema(
        description="Obtiene los detalles de un balance específico por su ID.",
        summary="Detalle de Balance",
        tags=["Balance"]
    ),
    create=extend_schema(
        description="Crea un nuevo balance con los datos proporcionados.",
        summary="Crear Balance",
        tags=["Balance"]
    ),
    update=extend_schema(
        description="Actualiza todos los campos de un balance existente.",
        summary="Actualizar Balance",
        tags=["Balance"]
    ),
    partial_update=extend_schema(
        description="Actualiza parcialmente los campos de un balance existente.",
        summary="Actualizar Parcialmente Balance",
        tags=["Balance"]
    ),
    destroy=extend_schema(
        description="Elimina un balance específico por su ID.",
        summary="Eliminar Balance",
        tags=["Balance"]
    ),
)

class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [IsAuthenticated]


@extend_schema_view(
    list=extend_schema(
        description="Obtiene una lista de todos los detalles de balances registrados.",
        summary="Lista de Detalles de Balance",
        tags=["DetalleBalance"]
    ),
    retrieve=extend_schema(
        description="Obtiene los detalles de un registro específico en el balance por su ID.",
        summary="Detalle de Balance",
        tags=["DetalleBalance"]
    ),
    create=extend_schema(
        description="Crea un nuevo detalle de balance con los datos proporcionados.",
        summary="Crear Detalle de Balance",
        tags=["DetalleBalance"]
    ),
    update=extend_schema(
        description="Actualiza todos los campos de un detalle de balance existente.",
        summary="Actualizar Detalle de Balance",
        tags=["DetalleBalance"]
    ),
    partial_update=extend_schema(
        description="Actualiza parcialmente los campos de un detalle de balance existente.",
        summary="Actualizar Parcialmente Detalle de Balance",
        tags=["DetalleBalance"]
    ),
    destroy=extend_schema(
        description="Elimina un detalle de balance específico por su ID.",
        summary="Eliminar Detalle de Balance",
        tags=["DetalleBalance"]
    ),
)

class DetalleBalanceViewSet(viewsets.ModelViewSet):
    queryset = DetalleBalance.objects.all()
    serializer_class = DetalleBalanceSerializer
    permission_classes = [IsAuthenticated]
