"""
URL configuration for LineaBalance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from Seguimiento.views import Report
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/', permanent=True)),  # Redirige la raíz al admin
    path('admin/', admin.site.urls),
    # path('', admin.site.urls),
    path('reportesbi/', login_required((Report.as_view())), name='reportesbi'),
    # path('api-auth/', include('rest_framework.urls'))
    path('api/v1/', include('Seguimiento.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(permission_classes=[IsAuthenticated],url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(permission_classes=[IsAuthenticated],url_name='schema'), name='redoc'),

]
