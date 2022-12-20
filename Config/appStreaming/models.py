from django.db import models


# Create your models here.

class Productor(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    mail = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class PaisDestino(models.Model):
    nombre = models.CharField(max_length=30)
    moneda = models.CharField(max_length=30)
def __str__(self):
        return self.nombre    

class Estado(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
def __str__(self):
        return self.nombre    

class PlataformaStream(models.Model):
    Nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
def __str__(self):
        return self.Nombre    

class CategoriaEvento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
def __str__(self):
        return self.nombre    

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
def __str__(self):
        return self.nombre    

class Estado(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
def __str__(self):
        return self.nombre    

class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    cantidadEntradas = models.IntegerField()
    artistasParticipantes = models.TextField()
    inicioStream = models.DateTimeField()
    finStream = models.DateField()
    fechaConfirmacion = models.DateTimeField()
    fechaRegistro = models.DateTimeField()
    link = models.CharField(max_length=30)
    urlImg = models.CharField(max_length=30)
   
   
    idProductor = models.ForeignKey('Productor', on_delete=models.CASCADE)
    def __str__(self):
        return self.idProductor
    idTipoEvento = models.ForeignKey('TipoEvento', on_delete=models.CASCADE)
    def __str__(self):
        return self.idTipoEvento
    idPlataforma = models.ForeignKey('PlataformaStream', on_delete=models.CASCADE)
    def __str__(self):
        return self.idPlataforma
    idEstado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    def __str__(self):
        return self.idEstado
    idPais = models.ForeignKey('PaisDestino', on_delete=models.CASCADE)
    def __str__(self):
        return self.idPais

