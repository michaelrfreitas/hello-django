"""This is a docstring which describes the module"""
from django.contrib import admin
from .models import Item

# Register your models here.
admin.site.register(Item)
