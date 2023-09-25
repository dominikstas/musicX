from django import forms
from .models import Plyta

class PlytaForm(forms.ModelForm):
    class Meta:
        model = Plyta
        fields = ['tytul', 'artysta', 'nosnik', 'rok_zakupu', 'zdjecie']