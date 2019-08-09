from django import forms 
from .models import Region, Commune


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['id_region', 'commune', 'region_name']
        labels = {
            "id_region": "Código Región",
            "commune": "Ciudad",
            "region_name": "Región"
        }


class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['id_commune', 'state', 'commune_name']
        labels = {
            "id_commune": "Código Ciudad",
            "state": "Estado",
            "commune_name": "Ciudad"
        }