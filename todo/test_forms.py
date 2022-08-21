"""This is a docstring which describes the module"""
from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    """This is a docstring which describes the module"""
    def test_item_name_is_required(self):
        """This is a docstring which describes the module"""
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """This is a docstring which describes the module"""
        form = ItemForm({'name': 'Test Todo Items'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """This is a docstring which describes the module"""
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
