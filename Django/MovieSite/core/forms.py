from django import forms
from datetime import datetime

from .models import Item


class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['title', 'overview']


class SearchAddItemForm(forms.Form):

    # page = forms.CharField(max_length=80)
    name = forms.CharField(max_length=80)
    release_year = forms.IntegerField(min_value=1500,
                                      max_value=datetime.now().year + 5,
                                      required=False)