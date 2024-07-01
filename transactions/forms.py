import datetime
from django import forms
from transactions import models
class RegistryItensForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.RegistryItens
        fields = "__all__"
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "unitary": forms.NumberInput(attrs={"class": "form-control"}),
            "favored": forms.TextInput(attrs={"class": "form-control"}),
        }
