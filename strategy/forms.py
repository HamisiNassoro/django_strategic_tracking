from django import forms
from .models import StrategicObjective, KeyActivity

class StrategicObjectiveForm(forms.ModelForm):
    class Meta:
        model = StrategicObjective
        fields = ['title', 'description']

class KeyActivityForm(forms.ModelForm):
    class Meta:
        model = KeyActivity
        fields = [
            'objective', 'activity_name', 'expected_output', 'output_indicators',
            'year1_target', 'year2_target', 'year3_target', 'year4_target',
            'year5_target', 'budget', 'responsibility', 'support'
        ]