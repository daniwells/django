from django import forms
from .models import Colaborator

class ColaboratorForm(forms.ModelForm):
    class Meta:
        model = Colaborator
        fields = ['EDV', 'full_name', 'responsibillity', 'sector', 'address', 'schedule_work', 'date_start', 'date_end', 'perfil_image']
        