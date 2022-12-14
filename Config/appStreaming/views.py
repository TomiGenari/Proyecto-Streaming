from django.shortcuts import render
from .forms import NuevoStreaming
from .forms import NuevoProductor
from .models import Evento
from .models import Productor
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    return render(request, "home.html", {})


def chose(request):
    eventos = Evento.objects.all()

    return render(request, "chose.html", {})


def eventosregistrados(request):
    eventos = Evento.objects.all()

    return render(request, "eventosregistrados.html", {})


def productor(request):
    productor = Productor.objects.all()
    if request.method == "POST":

        formularioBonito = NuevoProductor(request.POST)

        if formularioBonito.is_valid():

            formularioBonito.save()

    else:
        formularioBonito = NuevoProductor()

    return render(
        request,
        "register.html",
        {"formularioBonito": formularioBonito, "productor": productor},
    )


def inicio(request):
    eventos = Evento.objects.all()
    formito = NuevoStreaming()
    if request.method == "POST":

        formito = NuevoStreaming(request.POST)

        if formito.is_valid():

            formito.save()

    else:
        formito = NuevoStreaming()

    return render(request, "main.html", {"formito": formito, "eventos": eventos})


def eventosregistrados(request):
    eventos = Evento.objects.all()
    return render(request, 'eventosregistrados.html', {'eventos': eventos})