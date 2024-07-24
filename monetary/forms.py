import datetime
from django import forms
from monetary import models


class DateInput(forms.DateInput):
    input_type = "date"


class AccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Accounts
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"class": "form-control textarea", "rows": "3"}
            ),
            "balance": forms.NumberInput(attrs={"class": "form-control"}),
        }


class TransferForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].initial = datetime.date.today()

    class Meta:
        accounts = models.Accounts.objects.all()
        model = models.Transfers
        fields = "__all__"
        widgets = {
            "out_account": forms.Select(
                attrs={"class": "form-control"},
                choices=[(item.id, item.name) for item in accounts],
            ),
            "in_account": forms.Select(
                attrs={"class": "form-control"},
                choices=[(item.id, item.name) for item in accounts],
            ),
            "value": forms.NumberInput(attrs={"class": "form-control"}),
            "date": DateInput(
                format="%Y-%m-%d", attrs={"class": "form-control text-center"}
            ),
        }
