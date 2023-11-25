from django import forms
from .models import Emprendimiento

class EmprendimientoForm(forms.ModelForm):
    class Meta:
        model = Emprendimiento
        fields = ['nombre', 'descripcion', 'imagen', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer el campo de imagen opcional
        self.fields['imagen'].required = False