from django.test import TestCase
from .forms import PostForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'title', ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'title': 'Test Blog Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm
        self.assertEqual(form.Meta.fields['title', 'title_tag', 'author', 'body', 'header_image'])