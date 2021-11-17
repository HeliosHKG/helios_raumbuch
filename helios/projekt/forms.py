from django import forms
from .models import Projekt, ProjektSpezifikationen

class ProjektModelForm(forms.ModelForm):
    
    class Meta:
        model = Projekt 
        fields = (
            
            "projekt_name",
            "projekt_nummer",
            "projekt_beschreibung",
            "projekt_nutzung",
                    
            )  
        
        
class ProjektSpezModelForm(forms.ModelForm):
    
    class Meta: 
        model = ProjektSpezifikationen
        fields = (
            
            "projekt_raumnutzung",
            "projekt_raumflaeche",
            "projekt_raumflaeche",
        )