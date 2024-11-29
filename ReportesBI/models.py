from django.db import models

# Create your models here.
class EmptyModel(models.Model):
    pass

    class Meta:
        verbose_name = "Empty Model"
        verbose_name_plural = "Empty Models"

