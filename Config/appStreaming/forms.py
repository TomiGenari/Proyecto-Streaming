from django import forms
from .models import Evento
from django.contrib.auth.forms import UserCreationForm
from .models import Productor



class NuevoStreaming(forms.ModelForm):
    class Meta:
        model = Evento 
        fields = '__all__'
        
class NuevoProductor(forms.ModelForm):
    class Meta:
        model = Productor 
        fields = '__all__'

