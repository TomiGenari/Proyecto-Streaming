from django import forms
from .models import Evento, CategoriaEvento, Productor
from django.contrib.auth.forms import UserCreationForm


class NuevoStreaming(forms.ModelForm):
    class Meta:
        model = Evento 
        fields = '__all__'
    categorias = forms.ModelMultipleChoiceField(queryset=CategoriaEvento.objects.all())
        

class NuevoProductor(forms.ModelForm):
    class Meta:
        model = Productor 
        fields = '__all__'
