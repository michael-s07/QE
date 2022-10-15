from.models import Soaper_1, Soaper_2, Soaper_4, Plain_Dyeing
from django import forms
class soaper_1Form(forms.ModelForm):
    class Meta:
        model = Soaper_1
        fields = [
            'water_flow_comp_1',
            'water_temperatures_comp_1',
            'water_exit_comp_1',
            'water_flow_comp_2',
            'water_temperatures_comp_2',
            'water_flow_comp_3',
            'water_temperatures_comp_3',
            'staining'

        ]
        widgets = {
            'water_flow_comp_1': forms.Select(attrs={'class': 'form-control'}),
            'water_temperatures_comp_1':forms.Select(attrs={'class':'form-control'}),
            'water_exit_comp_1': forms.Select(attrs={'class': 'form-control'}),
            'water_flow_comp_2': forms.Select(attrs={'class': 'form-control'}),
            'water_temperatures_comp_2': forms.Select(attrs={'class': 'form-control'}),
            'water_flow_comp_3': forms.Select(attrs={'class': 'form-control'}),
            'water_temperatures_comp_3': forms.Select(attrs={'class': 'form-control'}),
            'staining': forms.Select(attrs={'class': 'form-control'})
        }

class soaper_2Form(forms.ModelForm):
    class Meta:
        model = Soaper_2
        fields = [
            'water_flow_comp_1',
            'water_temperatures_comp_1',
            'water_exit_comp_1',
            'water_flow_comp_2',
            'water_temperatures_comp_2',
            'water_flow_comp_3',
            'water_temperatures_comp_3',
            'staining'

        ]
        widgets = {
            'water_flow_comp_1': forms.Select(attrs={'class': 'form-control'}),
            'water_temperatures_comp_1':forms.Select(attrs={'class':'form-control'}),
            'water_exit_comp_1': forms.Select(attrs={'class': 'form-control'}),
            'water_flow_comp_2': forms.Select(attrs={'class': 'form-control'}),
            'water_temperatures_comp_2': forms.Select(attrs={'class': 'form-control'}),
            'water_flow_comp_3': forms.Select(attrs={'class': 'form-control'}),
            'water_temperatures_comp_3': forms.Select(attrs={'class': 'form-control'}),
            'staining': forms.Select(attrs={'class': 'form-control'})
        }

class soaper_4Form(forms.ModelForm):
    class Meta:
        model = Soaper_4
        fields = [
            'staining'

        ]
        widgets = {
            'staining': forms.Select(attrs={'class': 'form-control'})
        }

class plain_DyeingForm(forms.ModelForm):
    class Meta:
        model = Plain_Dyeing
        fields = [
            'beam_absorption',
            'other_defects'
        ]
        widgets = {
            'beam_absorption': forms.Select(attrs={'class': 'form-control'}),
            'other_defects':forms.Select(attrs={'class':'form-control'})
        }