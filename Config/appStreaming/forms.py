from django import forms
from .models import Evento, CategoriaEvento, Productor
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.utils import timezone


class NuevoStreaming(forms.ModelForm):
    class Meta:
        model = Evento 
        fields = '__all__'
        exclude = ['fechaConfirmacion']
    categorias = forms.ModelMultipleChoiceField(
        queryset=CategoriaEvento.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    inicioStream = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
    finStream = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
    fechaRegistro = forms.DateTimeField(initial=timezone.now)

class NuevoProductor(forms.ModelForm):
    class Meta:
        model = Productor 
        fields = '__all__'
