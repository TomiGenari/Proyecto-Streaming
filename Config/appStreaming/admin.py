from django.contrib import admin
from appStreaming.models import *
from .models import Estado
from .models import Evento
from .models import PlataformaStream
from .models import CategoriaEvento
from .models import TipoEvento
from .models import Productor
from .models import PaisDestino




admin.site.register(Evento)
admin.site.register(Estado)
admin.site.register(PlataformaStream)
admin.site.register(CategoriaEvento)
admin.site.register(TipoEvento)
admin.site.register(Productor)
admin.site.register(PaisDestino)

# Register your models here.
