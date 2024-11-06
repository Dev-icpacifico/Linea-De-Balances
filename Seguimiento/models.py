from django.db import models

# Create your models here.


class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    semana = models.IntegerField()
    fecha = models.DateField()

    class Meta:
        # managed = False
        db_table = 'Periodo'
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'
        unique_together = (('semana', 'fecha'),)

    def __str__(self):
        return str(self.semana) +"-"+ str(self.fecha)

class Partida(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'Partida'
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidaes'
        unique_together = (('nombre'),)
        ordering = ['nombre']

    def __str__(self):
        return str(self.nombre)


class Balance(models.Model):
    id = models.AutoField(primary_key=True)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Balance'
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'
        unique_together = (('partida', 'id'),)
        ordering = ['id']
    def __str__(self):
        return str(self.id)+ " - " +str(self.partida)

class DetalleBalance(models.Model):
    id = models.AutoField(primary_key=True)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    en_plan = models.BooleanField()
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    planificado = models.IntegerField()
    realizado = models.IntegerField()
    plan_acumulado = models.IntegerField()
    realizado_acumulado = models.IntegerField()
    proyeccion_media = models.IntegerField()
    proyeccion_acumulado_media = models.IntegerField()
    proyeccion_empirica = models.IntegerField()
    proyeccion_empirica_acumulada = models.IntegerField()



    class Meta:
        db_table = 'DetalleBalance'
        verbose_name = 'Detalle Balance'
        verbose_name_plural = 'Detalles Balances'
        unique_together = (('balance', 'periodo', 'id'),)
        ordering = ['id']

    def __str__(self):
        return str(self.id)