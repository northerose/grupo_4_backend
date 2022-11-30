from django import forms
from .models import Mascota


class PublicarForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = (
                    'nombre', 'foto', 'tipo', 'sexo', 'fecha_nacimiento',
                    'tamano_final', 'responsable', 'telefono', 'ubicacion',
                    'provincia','descripcion', 'desparasitado', 'vacunado', 
                    'castrado',
                )

