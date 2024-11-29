from rest_framework import serializers
from .models import *

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'
        # read_only_fields = ('id',)
        # write_only_fields = ('id',)
class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fase
        fields = '__all__'
        # depth = 1


class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'
        # depth = 1

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = '__all__'
        # depth = 1
class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'
        # depth = 2

class DetalleBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleBalance
        fields = '__all__'
        # depth = 1

