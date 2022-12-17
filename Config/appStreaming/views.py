from django.shortcuts import render
from .forms import NuevoStreaming
from .models import Evento
# Create your views here.



def inicio(request):
    eventos = Evento.objects.all()
    if request.method == 'POST':
        
        formito = NuevoStreaming(request.POST)
        
        if formito.is_valid():
            
            #PROCESAR LA INFORMACION
            
            formito.save()  
           
            
           
    else:
        formito = NuevoStreaming()
    
    return render(request, 'main.html', {'formito':formito,"eventos":eventos})
    
