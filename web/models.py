from django.db import models

# modelo  User de Django ser

from django.auth.models import User

class SimpleModel(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Ciudad(SimpleModel):
    pass

class Pais(SimpleModel):
    pass

class Entidad(models.Model):
    user = ForeignKey(User, related_name='persona')

    ciudad = ForeignKey(Ciudad)
    pais = ForeignKey(Pais)

    sitio_web = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    ip_registro = models.GenericIPAddressField()

    INACTIVO, ACTIVO, SUSPENDIDO = 0, 1, 2
    ESTADOS = (
        (INACTIVO, 'Inactivo'),
        (ACTIVO, 'Activo'),
        (SUSPENDIDO, 'Suspendido'),
    )
    estado = models.PositiveSmallInteger(choices=ESTADOS)

    class Meta:
        abstract = True

class Persona(Entidad):
    identificacion = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='persona_fotos/%Y/%m/%d')

    # Personas independientes tiene None en institucion
    institucion = ForeignKey(Institucion, null=True)
    cargo = models.CharField(max_length=100)
    actividad = models.TextField()

    areas_interes = models.TextField()


class Institucion(Entidad):
    nombre_abreviado = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='instituciones_logo/%Y/%m/%d')
    descripcion_general = models.TextField()
    mision = models.TextField()

    nombre_aplicante = models.CharField(max_length=200)
    nombre_encargado = models.CharField(max_length=200)

    recursos_ofrece = models.TextField()

class SolicitudAdherencia(models.Model):
    persona = models.ForeighKey(Persona)
    institucion = models.ForeignKey(Institucion)
    fecha = models.DateTimeField()

class Privacidad(models.Model):
    demografica = models.BooleanField(default=True)
    contacto = models.BooleanField(default=True)

    class Meta:
        abstract = True

class PrivacidadPersona(Privacidad):
    institucion = models.BooleanField(default=True)

class PrivacidadInstitucion(Privacidad):
    ofertas = models.BooleanField(default=True)
    demandas = models.BooleanField(default=True)
    alcance_incubacion = models.BooleanField(default=True)
    alcance_consursos = models.BooleanField(default=True)

class Mensaje(models.Model):
    emisor = models.ForeignKey(User)
    remitente = models.ForeignKey(User)
    fecha = models.DateTimeField()
    texto = models.TextField()
