from django import forms 
from .models import players
class playerform(forms.ModelForm):
    class Meta:
        model=players
        fields=['firstname','lastname','age','phone','signed']
class playeridform(forms.Form):
    id=forms.IntegerField(label='Enter Id ',min_value=1)
    
   