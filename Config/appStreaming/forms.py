from django import forms
from .models import Evento



class NuevoStreaming(forms.ModelForm):
    class Meta:
        model = Evento 
        fields = '__all__'
        

       