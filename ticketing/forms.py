from django import forms
from .models import Cinema

class ShowTimeSearchForm(forms.Form):
    movie_name = forms.CharField(max_length=100, label='نام فیلم', required=False)