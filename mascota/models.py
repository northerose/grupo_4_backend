from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class TipoMascota(models.TextChoices):
    gato = 'g', _('Gato')
    perro = 'p', _('Perro')

class SexoMascota(models.TextChoices):
    hembra = 'h', _('Hembra')
    macho = 'm', _('Macho')

class TamanoMascota(models.TextChoices):
    pequeno = 'p', _('Pequeño')
    mediano = 'm', _('Mediano')
    grande = 'g', _('Grande')

class Provincia(models.TextChoices):
    buenos_aires = 'Ciudad Autónoma de Buenos Aires', _('Ciudad Autónoma de Buenos Aires') 
    catamarca = 'Catamarca', _('Catamarca') 
    chaco = 'Chaco', _('Chaco')
    chubut = 'Chubut', _('Chubut')
    cordoba = 'Córdoba', _('Córdoba')
    corrientes = 'Corrientes', _('Corrientes')
    entre_rios = 'Entre Ríos', _('Entre Ríos')
    formosa = 'Formosa', _('Formosa')    
    jujuy = 'Jujuy', _('Jujuy') 
    pampa = 'Pampa', _('La Pampa')
    rioja = 'La Rioja', _('La Rioja')
    mendoza = 'Mendoza', _('Mendoza')   
    misiones = 'Misiones', _('Misiones')
    neuquen = 'Neuquén', _('Neuquén')
    rio_negro = 'Río Negro', _('Río Negro')
    salta = 'Salta', _('Salta')
    san_juan = 'San Juan', _('San Juan')
    san_luis = 'San Luis', _('San Luis')
    santa_cruz = 'Santa Cruz', _('Santa Cruz')
    santa_fe = 'Santa Fé', _('Santa Fé')
    santiago = 'Santiago del Estero', _('Santiago del Estero')
    fuego = 'Tierra del Fuego', _('Tierra del Fuego')
    tucuman = 'Tucumán', _('Tucumán')


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(null=True, upload_to='imagenes')
    tipo = models.CharField(max_length=2, choices=TipoMascota.choices)
    sexo = models.CharField(max_length=2, choices=SexoMascota.choices)
    fecha_nacimiento = models.DateField()
    tamano_final = models.CharField(max_length=2, choices=TamanoMascota.choices)
    responsable = models.CharField(max_length=100)
    telefono = models.IntegerField()
    ubicacion = models.CharField(max_length=200)
    provincia = models.CharField(null=True, max_length=200, choices=Provincia.choices)
    descripcion = models.TextField()
    desparasitado = models.BooleanField()
    vacunado = models.BooleanField()
    castrado = models.BooleanField()

    def __str__(self):
        return self.nombre
