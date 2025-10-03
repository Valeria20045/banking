from django import forms
from .models import Countries

class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = ['name', 'abrev', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'abrev': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
