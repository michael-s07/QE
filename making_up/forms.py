from django import forms
from .models import Finishing_Pieces

class finishing_PiecesForm(forms.ModelForm):
    class Meta:
        model =  Finishing_Pieces
        fields = [
            'specification_check_on_defects',
            'Quality_of_labeling'

        ]
        widgets = {
            'specification_check_on_defects': forms.Select(attrs={'class': 'form-control'}),
            'Quality_of_labeling':forms.Select(attrs={'class':'form-control'})
        }