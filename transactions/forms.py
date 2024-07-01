import datetime
from django import forms
from transactions import models
class PaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].initial = datetime.date.today()

    class Meta:
        model = models.Payments
        fields = "__all__"
        widgets = {
            "date": DateInput(
                format="%Y-%m-%d", attrs={"class": "form-control text-center"}
            )
        }


class RegistriesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].initial = datetime.date.today()
        self.fields["value"].initial = "0.00"

    class Meta:
        companies = models.Companies.objects.all()
        categories = models.Categories.objects.all()
        model = models.Registries
        fields = "__all__"
        widgets = {
            "date": DateInput(
                format="%Y-%m-%d", attrs={"class": "form-control text-center"}
            ),
            "companies": forms.Select(
                attrs={"class": "form-control"},
                choices=[(item.id, item.name) for item in companies],
            ),
            "category_n1": forms.Select(
                attrs={"class": "form-control"},
                choices=[(item.id, item.description) for item in categories],
            ),
            "category_n2": forms.Select(
                attrs={"class": "form-control"},
                choices=[(item.id, item.description) for item in categories],
            ),
            "category_n3": forms.Select(
                attrs={"class": "form-control"},
                choices=[(item.id, item.description) for item in categories],
            ),
            "value": forms.NumberInput(
                attrs={"class": "form-control text-right"}
            ),
            "in_out": forms.Select(
                attrs={"class": "form-control text-center"},
                choices=[("DÉBITO", "DÉBITO"), ("CRÉDITO", "CRÉDITO")],
            ),
            "ordering": forms.NumberInput(
                attrs={"class": "form-control text-right"}
            ),
            "obs": forms.Textarea(
                attrs={"class": "form-control textarea", "rows": "3"}
            ),
        }


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
