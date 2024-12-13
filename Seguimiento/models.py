from django.db import models

# Create your models here.

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) +" - " + str(self.nombre_proyecto)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['nombre_proyecto']
        unique_together = ('nombre_proyecto',)

class Fase(models.Model):
    id = models.AutoField(primary_key=True)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre_fase = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.Proyecto.nombre_proyecto) +" - " + str(self.nombre_fase)

    class Meta:
        verbose_name = 'Fase'
        verbose_name_plural = 'Fases'
        ordering = ['nombre_fase']
        # unique_together = ('nombre_fase','Proyecto',)

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
        verbose_name_plural = 'Partidas'
        unique_together = ('nombre',)
        ordering = ['nombre']

    def __str__(self):
        return str(self.nombre)


class Balance(models.Model):
    id = models.AutoField(primary_key=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)


    class Meta:
        db_table = 'Balance'
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'
        unique_together = (('partida', 'id'),)
        ordering = ['id']
    def __str__(self):
        return str(self.id)+ " - " +str(self.partida) + " - " + str(self.fase)

class DetalleBalance(models.Model):
    id = models.AutoField(primary_key=True)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    en_plan = models.BooleanField(verbose_name = "En Plan",help_text="Indica si el registro está dentro del periodo planificado")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    semana_trabajo = models.IntegerField(verbose_name = "S.Lab",blank=True, null=True, help_text="Semana laboral del proyecto")
    planificado = models.IntegerField(verbose_name = "Q.Plan", blank= True, null=True, help_text="Cantidad Planificada")
    realizado = models.IntegerField(verbose_name = "Q.Real", blank=True, null=True, help_text="Cantidad Realizada")
    proyeccion_empirica = models.IntegerField(verbose_name = "Py Em", blank=True, null=True, help_text="Proyección Empírica")
    proyeccion_media = models.IntegerField(verbose_name = "Py Md", blank=True, null=True, help_text="Proyección Media")
    plan_acumulado = models.IntegerField(verbose_name = "Plan Ac", blank=True, null=True, help_text="Plan Acumulado")
    realizado_acumulado = models.IntegerField(verbose_name = "Real Ac", blank=True, null=True, help_text="Realizado Acumulado")
    proyeccion_acumulado_media = models.IntegerField(verbose_name = "Py Md Ac", blank=True, null=True, help_text="Proyección media acumulado")
    proyeccion_empirica_acumulada = models.IntegerField(verbose_name = "Py Em Ac", blank=True, null=True, help_text="Proyección empírica acumulado")


    class Meta:
        db_table = 'DetalleBalance'
        verbose_name = 'Detalle Balance'
        verbose_name_plural = 'Detalles Balances'
        unique_together = (('balance', 'periodo', 'id'),)
        ordering = ['id']

    def __str__(self):
        return str(self.id)

    """    def save(self, *args, **kwargs):
            # Guardar primero para obtener el ID (en caso de que sea un nuevo registro)
            super().save(*args, **kwargs)

            # Paso 1: Configurar los valores de proyeccion_empirica_acumulada en None para los registros anteriores
            DetalleBalance.objects.filter(
                balance=self.balance,
                periodo=self.periodo,
                id__lt=self.id
            ).update(proyeccion_empirica_acumulada=None)

            # Paso 2: Asignar el valor de realizado_acumulado del registro actual al registro anterior
            registro_anterior = DetalleBalance.objects.filter(
                balance=self.balance,
                periodo=self.periodo,
                id__lt=self.id
            ).order_by('-id').first()

            if registro_anterior:
                registro_anterior.proyeccion_empirica_acumulada = self.realizado_acumulado
                registro_anterior.save()

            # Paso 3: Calcular la proyección empírica acumulada desde el registro actual en adelante
            proyeccion_acumulada = self.realizado_acumulado
            registros_posteriores = DetalleBalance.objects.filter(
                balance=self.balance,
                periodo=self.periodo,
                id__gte=self.id
            ).order_by('id')

            for registro in registros_posteriores:
                if registro.proyeccion_empirica is not None:
                    proyeccion_acumulada += registro.proyeccion_empirica
                    registro.proyeccion_empirica_acumulada = proyeccion_acumulada
                else:
                    registro.proyeccion_empirica_acumulada = None
                registro.save()

            super().save(*args, **kwargs)"""