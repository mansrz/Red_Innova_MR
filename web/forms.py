from django import forms
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from web.models import Persona, Institucion, User

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre_abreviado','ciudad','pais','sitio_web','telefono','email',
                 'descripcion_general','logo','mision','nombre_aplicante','nombre_encargado',
                 'recursos_ofrece']
 
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['ciudad','pais','sitio_web','telefono','email',
                 'foto','cargo','institucion','cargo','actividad',
                 'areas_interes','identificacion']
 

class UserForm(DjangoUserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'special'}),label='Nombre de Usuario')
    #tipo = forms.IntegerField(widget= forms.HiddenInput(), initial = 1)
    class Meta:
        model = User
        fields = ['username', 'password']

        


