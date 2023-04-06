from django import forms

from .models import Degree


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ('title_degree', 'first_name', 'last_name', 'date_of_birth', 'date_degree', 'vote', 'hash', 'txId')


