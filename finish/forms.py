from django import forms
from .models import Stenter_5, Stenter_7, Calender, Baking_Oven

class stenter_5Form(forms.ModelForm):
    class Meta:
        model = Stenter_5
        fields = [
            'straightness_of_design',
            'straightness_of_fibre',
            'moisture_outfeed_cloth_with'
        ]

        widgets = {
            'straightness_of_design': forms.Select(attrs={'class': 'form-control'}),
            'straightness_of_fibre':forms.Select(attrs={'class':'form-control'}),
            'moisture_outfeed_cloth_with': forms.Select(attrs={'class': 'form-control'})
        }


class stenter_7Form(forms.ModelForm):
    class Meta:
        model = Stenter_7
        fields = [
            'straightness_of_design',
            'straightness_of_fibre',
            'moisture_outfeed_cloth_with'
        ]

        widgets = {
            'straightness_of_design': forms.Select(attrs={'class': 'form-control'}),
            'straightness_of_fibre':forms.Select(attrs={'class':'form-control'}),
            'moisture_outfeed_cloth_with': forms.Select(attrs={'class': 'form-control'})
        }

class calenderForm(forms.ModelForm):
    class Meta:
        model = Calender
        fields = [
            'eveness_of_shiny_effect',
            'temperature',
            'speed_fancy_woodin_dumas'
        ]
        widgets = {
            'eveness_of_shiny_effect': forms.Select(attrs={'class': 'form-control'}),
            'temperature':forms.Select(attrs={'class':'form-control'}),
            'speed_fancy_woodin_dumas': forms.Select(attrs={'class': 'form-control'})
        }

class bakingOvenForm(forms.ModelForm):
    class Meta:
        model =  Baking_Oven
        fields = [
            'loop',
            'spread',
            'residence_time',
            'temperature'
        ]
        widgets = {
            'loop': forms.Select(attrs={'class': 'form-control'}),
            'spread':forms.Select(attrs={'class':'form-control'}),
            'residence_time': forms.Select(attrs={'class': 'form-control'}),
            'temperature': forms.Select(attrs={'class': 'form-control'})
        }