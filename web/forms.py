from django import forms
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from web.models import Persona, Institucion

class InstitucionForm(forms.ModelForm)
    class Meta:
        model = Institucion
        fields = ['nombre_abreviado','ciudad','pais',\
                 'sitio_web','telefono','email','estado'\
                 ,'descripcion_general','logo','mision'\
                 ,'nombre_aplicante','nombre_encargado'\
                 ,'recursos_ofrece']
 
class PersonaForm(forms.ModelForm)
    class Meta:
        model = Institucion
        fields = ['name','ciudad','pais',\
                 'sitio_web','telefono','email','estado'\
                 ,'descripcion_general','foto','cargo'\
                 ,'institucion','cargo','actividad'\
                 ,'areas_interes','identificacion']
 


        


