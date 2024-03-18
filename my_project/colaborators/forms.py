from django import forms
from .models import Colaborator

class ColaboratorForm(forms.ModelForm):
    class Meta:
        model = Colaborator
        fields = ['EDV', 'full_name', 'responsibillity', 'sector', 'address', 'date_admission', 'schedule_start', 'schedule_end', 'perfil_image']
        