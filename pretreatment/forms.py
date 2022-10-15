from django import forms
from .models import Singeing, Desizing_mangle, Washing_Machine_1, Saturator_1_NaOH, J_Box_1_Scouring ,Washing_Machine_2 ,Saturator_2_H2O2 ,J_Box_2_Bleaching ,Washing_Machine_3 ,Merceriser ,Stenter_6

class singelingForm(forms.ModelForm):
    class Meta:
        model = Singeing
        fields = [
            'flame_distribution',
            'colour_of_flame',
            'speed'
        ]
        widgets = {
            'flame_distribution': forms.Select(attrs={'class': 'form-control'}),
            'colour_of_flame':forms.Select(attrs={'class':'form-control'}),
            'speed': forms.Select(attrs={'class': 'form-control'})
        }

class desizing_mangleForm(forms.ModelForm):
    class Meta:
        model = Desizing_mangle
        fields = [
            'temperature',
            'impregnation'
        ]
        widgets = {
            'temperature': forms.Select(attrs={'class': 'form-control'}),
            'impregnation':forms.Select(attrs={'class':'form-control'})
        }

class saturator_1Form(forms.ModelForm):
    class Meta:
        model = Saturator_1_NaOH
        fields = [
            'squeezing_mangle_pressure',
            'level',
            'density_and_circulation',
            'end_point_NaOH'
        ]
        widgets = {
            'loop': forms.Select(attrs={'class': 'form-control'}),
            'spread':forms.Select(attrs={'class':'form-control'}),
            'residence_time': forms.Select(attrs={'class': 'form-control'}),
            'temperature': forms.Select(attrs={'class': 'form-control'})
        }

class j_box1Form(forms.ModelForm):
    class Meta:
        model = J_Box_1_Scouring
        fields = [
            'loading_speed',
            'volume_of_cloth_in_j_box',
            'flow_from_overflow_pipe',
            'temperature_and_stream_flow'
        ]
        widgets = {
            'loop': forms.Select(attrs={'class': 'form-control'}),
            'spread':forms.Select(attrs={'class':'form-control'}),
            'residence_time': forms.Select(attrs={'class': 'form-control'}),
            'temperature': forms.Select(attrs={'class': 'form-control'})
        }

class washing_machine2Form(forms.ModelForm):
    class Meta:
        model = Washing_Machine_2
        fields = [
            'temperature',
            'fresh_water_flow'
        ]

class saturator_2Form(forms.ModelForm):
    class Meta:
        model = Saturator_2_H2O2
        fields = [
            'level',
            'end_point_H2O2',
            'squeezing_mangle_pressure'

        ]

class j_box2Form(forms.ModelForm):
    class Meta:
        model = J_Box_2_Bleaching
        fields = [
            'volume_of_cloth_in_j_box',
            'flow_from_overflow_pipe'
        ]

class washing_machine1Form(forms.ModelForm):
    class Meta:
        model = Washing_Machine_1
        fields = [
            'temperature',
            'fresh_water_flow',
            'starch_test'

        ]

class washing_machine3Form(forms.ModelForm):
    class Meta:
        model = Washing_Machine_3
        fields = [
            'temperature',
            'fresh_water_flow'
        ]

class merceriserForm(forms.ModelForm):
    class Meta:
        model = Merceriser
        fields = [
            'rectofact_performance',
            'fibre_deviation',
            'folded_selvedge_at_in_the_feed_impregnation_mangle',
            'strong_caustic_concentration',
            'check_on_in_feed_or_chain_clips',
            'flow_on_spraying_units',
            'pressure_suction_units_1_to_6',
            'water_flow_from_washing_units_to_lagoon',
            'lagoon_temperature',
            'water_flow_to_washing_units',
            'week_caustic_concentration',
            'final_width_of_mercerised_cloth',
            'caustic_check_Phenolphthalein_drop'
        ]
        widgets = {
            'rectofact_performance': forms.Select(attrs={'class': 'form-control'}),
            'fibre_deviation':forms.Select(attrs={'class':'form-control'}),
            'folded_selvedge_at_in_the_feed_impregnation_mangle': forms.Select(attrs={'class': 'form-control'}),
            'strong_caustic_concentration': forms.Select(attrs={'class': 'form-control'}),
            'check_on_in_feed_or_chain_clips': forms.Select(attrs={'class': 'form-control'}),
            'flow_on_spraying_units':forms.Select(attrs={'class':'form-control'}),
            'pressure_suction_units_1_to_6': forms.Select(attrs={'class': 'form-control'}),
            'water_flow_from_washing_units_to_lagoon': forms.Select(attrs={'class': 'form-control'}),
            'lagoon_temperature': forms.Select(attrs={'class': 'form-control'}),
            'water_flow_to_washing_units': forms.Select(attrs={'class': 'form-control'}),
            'week_caustic_concentration': forms.Select(attrs={'class': 'form-control'}),
            'final_width_of_mercerised_cloth': forms.Select(attrs={'class': 'form-control'}),
            'caustic_check_Phenolphthalein_drop': forms.Select(attrs={'class': 'form-control'})
        }

class stenter_6Form(forms.ModelForm):
    class Meta:
        model = Stenter_6
        fields = [
            'Rectofact_performance',
            'fibre_deviation',
            'impregnation_temperature',
            'check_on_in_feed_clips',
            'drying_temperature_6_chambers',
            'end_moisture',
            'width_of_beam'
        ]
        widgets = {
            'Rectofact_performance': forms.Select(attrs={'class': 'form-control'}),
            'fibre_deviation':forms.Select(attrs={'class':'form-control'}),
            'impregnation_temperature': forms.Select(attrs={'class': 'form-control'}),
            'check_on_in_feed_clips': forms.Select(attrs={'class': 'form-control'}),
            'drying_temperature_6_chambers': forms.Select(attrs={'class': 'form-control'}),
            'end_moisture': forms.Select(attrs={'class': 'form-control'}),
            'width_of_beam': forms.Select(attrs={'class': 'form-control'})
        }