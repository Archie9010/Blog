from django.test import TestCase
# from .models import Item


class TestViews(TestCase):

    def test_get_base(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')