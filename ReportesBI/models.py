from django.db import models

# Create your models here.
class ReportBi(models.Model):
    enlace_reporte = models.TextField("Enlace reporte BI")

    class Meta:
        db_table = 'reportbi'
        verbose_name = 'Reporte BI'
        verbose_name_plural = 'Reportes BI'


