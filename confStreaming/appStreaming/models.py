from django.db import models


# Create your models here.

class Productor(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField()
    telefono = models.IntegerField()
    mail = models.CharField()
    password = models.CharField()

class PaisDestino(models.Model):
    nombre = models.CharField()
    moneda = models.CharField()

class Estado(models.Model):
    nombre = models.CharField()
    descripcion = models.CharField()

class PlataformaStream(models.Model):
    nombre = models.CharField()
    descripcion = models.CharField()

class CategoriaEvento(models.Model):
    nombre = models.CharField()
    descripcion = models.CharField()

class TipoEvento(models.Model):
    nombre = models.CharField()
    descripcion = models.CharField()

class Estado(models.Model):
    nombre = models.CharField()
    descripcion = models.CharField()

class Evento(models.Model):
    nombre = models.CharField()
    descripcion = models.TextField()
    cantidadEntradas = models.IntegerField()
    artistasParticipantes = models.TextField()
    inicioStream = models.DateTimeField()
    finStream = models.DateTimeField()
    fechaConfirmacion = models.DateTimeField()
    fechaRegistro = models.DateTimeField()
    link = models.CharField()
    urlImg = models.CharField()
    
    idProductor = models.ForeignKey(Productor)
    idTipoEvento = models.ForeignKey(TipoEvento)
    idPlataforma = models.ForeignKey(PlataformaStream)
    idEstado = models.ForeignKey(Estado)
    idPais = models.ForeignKey(PaisDestino)

