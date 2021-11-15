from django import forms

from .models import Test


class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ['name', 'age', 'comment']
        labels = {'name': ''}