from django.db import router
from django.urls import path, include
from rest_framework import routers

# from LineaBalance.urls import urlpatterns
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

"""from .views import Report

urlpatterns = [
    # Urls Base
    path('reportbi', Report.as_view(), name="reportebi"),

]"""

routers = routers.DefaultRouter()
routers.register(r'Proyectos', ProyectoViewSet)
routers.register(r'Fases', FaseViewSet)
routers.register(r'periodos', PeriodoViewSet)
routers.register(r'Partidas', PartidaViewSet)
routers.register(r'Balances', BalanceViewSet)
routers.register(r'Detallebalances', DetalleBalanceViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
