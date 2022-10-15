from .models import Adepa_Base_Nustyle_Safoa, Steamer, OWS
from django import forms

class adepa_Base_Nustyle_SafoaForm(forms.ModelForm):
    class Meta:
        model = Adepa_Base_Nustyle_Safoa
        fields = [
            'drying_temperature',
            'speed',
            'base_colour_misfit',
            'selvedge_effect',
            'white_patches',
            'color_marking_off',
            'other_defect'

        ]
        widgets = {
            'drying_temperature': forms.Select(attrs={'class': 'form-control'}),
            'speed':forms.Select(attrs={'class':'form-control'}),
            'base_colour_misfit': forms.Select(attrs={'class': 'form-control'}),
            'selvedge_effect': forms.Select(attrs={'class': 'form-control'}),
            'white_patches': forms.Select(attrs={'class': 'form-control'}),
            'color_marking_off':forms.Select(attrs={'class':'form-control'}),
            'other_defect': forms.Select(attrs={'class': 'form-control'})
        }

class steamerForm(forms.ModelForm):
    class Meta:
        model = Steamer
        fields = [
            'temperature',
            'speed'
        ]
        widgets = {
            'temperature': forms.Select(attrs={'class': 'form-control'}),
            'speed':forms.Select(attrs={'class':'form-control'})
        }

class owsForm(forms.ModelForm):
    class Meta:
        model = OWS
        fields = [
            'temperatures_washing',
            'units_squeezing_pressures'
        ]
        widgets = {
            'temperatures_washing': forms.Select(attrs={'class': 'form-control'}),
            'units_squeezing_pressures':forms.Select(attrs={'class':'form-control'})
        }
