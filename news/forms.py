from django import forms
from .models import preordery

class PlytaForm(forms.ModelForm):
    class Meta:
        model = preordery
        fields = ['tytul', 'artysta', 'nosnik', 'data', 'zdjecie']
        labels = {
            'tytul': 'Title',
            'artysta': 'Artist',
            'nosnik': 'Media Type',
            'data': 'Delivery date',
            'zdjecie': 'Cover Image',
        }
