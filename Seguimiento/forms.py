from django import forms
from django.forms import NumberInput
from .models import DetalleBalance

class DetalleBalanceForm(forms.ModelForm):
    class Meta:
        model = DetalleBalance
        fields = '__all__'
        widgets = {
            'semana_trabajo': NumberInput(attrs={'size': 3}),
            'planificado': NumberInput(attrs={'size': 3}),
            'realizado': NumberInput(attrs={'size': 3}),
            'plan_acumulado': NumberInput(attrs={'size': 10}),
            'realizado_acumulado': NumberInput(attrs={'size': 3}),
            'proyeccion_media': NumberInput(attrs={'size': 3}),
            'proyeccion_acumulado_media': NumberInput(attrs={'size': 3}),
            'proyeccion_empirica': NumberInput(attrs={'size': 3}),
            'proyeccion_empirica_acumulada': NumberInput(attrs={'size': 3}),
        }
