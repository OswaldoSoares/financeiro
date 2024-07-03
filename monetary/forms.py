import datetime
from django import forms
from monetary import models


class DateInput(forms.DateInput):
    input_type = "date"
