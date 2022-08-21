"""This is a docstring which describes the module"""
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """This is a docstring which describes the module"""
    class Meta:
        """This is a docstring which describes the module"""
        model = Item
        fields = ['name', 'done']
