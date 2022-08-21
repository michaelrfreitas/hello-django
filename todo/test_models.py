"""This is a docstring which describes the module"""
from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    """This is a docstring which describes the module"""

    def test_done_defaults_to_false(self):
        """This is a docstring which describes the module"""
        # pylint: disable=no-member
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        """This is a docstring which describes the module"""
        # pylint: disable=no-member
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
