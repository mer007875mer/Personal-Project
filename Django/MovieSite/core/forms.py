from django import forms
from datetime import datetime


class AddItemForm(forms.Form):

    page = forms.CharField(max_length=80)
    name = forms.CharField(max_length=80)
    include_adult = forms.BooleanField(required=False, initial=False)
    release_year = forms.IntegerField(min_value=1500,
                                      max_value=datetime.now().year + 5,
                                      required=False)