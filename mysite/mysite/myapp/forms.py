from django import forms 
class Formgood(forms.Form):           
    brand = forms.CharField(required=True,max_length=20)
    name = forms.CharField(required=True,max_length=20)
    number = forms.CharField(required=True,max_length=20)
    version = forms.CharField(required=True,max_length=40)
    class_field = forms.CharField( required=True,max_length=20)  
    # Field renamed because it was a Python reserved word.
    price = forms.FloatField(required=True)