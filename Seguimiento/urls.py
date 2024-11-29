from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

"""from .views import Report

urlpatterns = [
    # Urls Base
    path('reportbi', Report.as_view(), name="reportebi"),

]"""