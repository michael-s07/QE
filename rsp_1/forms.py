from django import forms

from .models import Double_run_institution_woodin

class rsp1Form(forms.ModelForm):
    class Meta:
        model = Double_run_institution_woodin
        fields = [
            'drying_temperature',
            'speed',
            'cloth_width',
            'beam_position',
            'lattice_roller',
            'vision_system',
            'colour_pumps',
            'check_fitting',
            'penetration',
            'colour_marking_off',
            'other_defects'
        ]
        widgets = {
            'drying_temperature': forms.Select(attrs={'class': 'form-control'}),
            'speed':forms.Select(attrs={'class':'form-control'}),
            'cloth_width': forms.Select(attrs={'class': 'form-control'}),
            'beam_position': forms.Select(attrs={'class': 'form-control'}),
            'lattice_roller': forms.Select(attrs={'class': 'form-control'}),
            'vision_system':forms.Select(attrs={'class':'form-control'}),
            'colour_pumps': forms.Select(attrs={'class': 'form-control'}),
            'check_fitting': forms.Select(attrs={'class': 'form-control'}),
            'penetration': forms.Select(attrs={'class': 'form-control'}),
            'colour_marking_off': forms.Select(attrs={'class': 'form-control'}),
            'other_defects': forms.Select(attrs={'class': 'form-control'})
        }