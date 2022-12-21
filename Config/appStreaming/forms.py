from django import forms
from .models import Evento
from django.contrib.auth.forms import UserCreationForm
from .models import Productor


class DateTimeInput(forms.DateTimeInput):
	input_type = 'date'



class NuevoStreaming(forms.ModelForm):
    class Meta:
        model = Evento 
        fields = '__all__'
        
        widgets = {
            'inicioStream' : DateTimeInput(),
            'finStream' : DateTimeInput(),
            'fechaConfirmacion' : DateTimeInput(),
            'fechaRegistro' : DateTimeInput(),
        }
        
        

class NuevoProductor(forms.ModelForm):
    class Meta:
        model = Productor 
        fields = '__all__'
