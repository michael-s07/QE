from django import forms
from .models import Woodin_institution

class woodin_institutionForm(forms.ModelForm):
    class Meta:
        model = Woodin_institution
        fields = [
            'drying_temperature',
            'speed',
            'cloth_width_total',
            'check_on_fitting',
            'penetration',
            'colour_marking_off',
            'printing_folds',
            'other_defects'

        ]
        widgets = {
            'drying_temperature': forms.Select(attrs={'class': 'form-control'}),
            'speed':forms.Select(attrs={'class':'form-control'}),
            'cloth_width_total': forms.Select(attrs={'class': 'form-control'}),
            'check_on_fitting': forms.Select(attrs={'class': 'form-control'}),
            'penetration': forms.Select(attrs={'class': 'form-control'}),
            'colour_marking_off':forms.Select(attrs={'class':'form-control'}),
            'printing_folds': forms.Select(attrs={'class': 'form-control'}),
            'other_defects': forms.Select(attrs={'class': 'form-control'})
        }