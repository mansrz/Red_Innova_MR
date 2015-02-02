# -*- coding: utf-8 -*-
from django.db import models

# modelo  User de Django ser

from django.contrib.auth.models import User

class SimpleModel(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Ciudad(SimpleModel):
    pass

class Pais(SimpleModel):
    pass

class Entidad(models.Model):
    user = models.ForeignKey(User)

    ciudad = models.ForeignKey(Ciudad)
    pais = models.ForeignKey(Pais)

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
    estado = models.PositiveSmallIntegerField(choices=ESTADOS)

    class Meta:
        abstract = True

class Persona(Entidad):
    identificacion = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='persona_fotos/%Y/%m/%d')

    # Personas independientes tiene None en institucion
    institucion = models.ForeignKey('Institucion', null=True)
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
    persona = models.ForeignKey(Persona)
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
    emisor = models.ForeignKey(User, related_name='+')
    remitente = models.ForeignKey(User, related_name='+')
    fecha = models.DateTimeField()
    texto = models.TextField()

class Recomendacion(models.Model):
    emisor = models.ForeignKey(User, related_name='+')
    remitente = models.ForeignKey(User, related_name='+')
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()
    estrellas = models.PositiveSmallIntegerField()
    # TODO demanda/oferta/lo-que-sea que se se recomiende

class Publicacion(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)

    fecha_limite = models.DateField()

    dominio = models.CharField(max_length=200)
    subdominio = models.CharField(max_length=200)

    lugar = models.CharField(max_length=200)

    #Beneficiario es usuario final (Descripcion)
    perfil_beneficiario = models.TextField()
    #Cliente es usuario que invierte (Descripcion)
    perfil_cliente = models.TextField()

    descripcion_soluciones = models.TextField(null = True)

    DESACTIVADA, ACTIVA, TERMINADA, CENSURADA = 0, 1, 2, 3
    ESTADOS = (
        (DESACTIVADA, 'Desactivada'),
        (ACTIVA, 'Activa'),
        (TERMINADA, 'Terminada'),
        (CENSURADA, 'Censurada'),
    )
    estado = models.PositiveSmallIntegerField(choices=ESTADOS)

    # TODO: ambito, alcance, privacidad

class Demanda(Publicacion):
    descripcion_importancia = models.TextField()

    #Control de versiones.
    nombre_instancia = models.CharField(max_length=200, null=True)
    padre = models.ForeignKey('self', null=True)


class Oferta(Publicacion):

    TECNOLOGIA, PROTOTIPO, EMPRENDIMIENTO = 0, 1, 2
    TIPOS = (
        (TECNOLOGIA, 'Tecnología'),
        (PROTOTIPO, 'Prototipo'),
        (EMPRENDIMIENTO, 'Emprendimiento'),
    )
    tipo = models.PositiveSmallIntegerField(choices=TIPOS)

    descripcion_propuesta_valor = models.TextField()

    bmc = models.FileField(upload_to='ofertas_bmc/%Y/%m/%d')
    porter = models.FileField(upload_to='ofertas_porter/%Y/%m/%d')
    cuadro_competidores = models.FileField(upload_to='ofertas_competidores/%Y/%m/%d')
    cuadro_tendencias = models.FileField(upload_to='ofertas_tendencias/%Y/%m/%d')

    foto = models.ImageField(upload_to='oferta_foto/%Y/%m/%d')

    estado_propiedad_intelectual = models.CharField(max_length=100, null=True)

    evidencia_traccion = models.TextField(null=True)

    equipo = models.TextField()
    roles_equipos = models.TextField()

class Incubacion(models.Model):
    fecha_inicio = models.DateField()
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    condiciones = models.TextField()
    descripcion_ofertas = models.TextField()
    TECNOLOGIA, PROTOTIPO, EMPRENDIMIENTO = 0, 1, 2
    TIPOS = (
        (TECNOLOGIA, 'Tecnología'),
        (PROTOTIPO, 'Prototipo'),
        (EMPRENDIMIENTO, 'Emprendimiento'),
    )
    tipo = models.PositiveSmallIntegerField(choices=TIPOS)
    #TODO alcance







