from django import forms

class CrearAuto(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    
class BuscarAuto(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    

    