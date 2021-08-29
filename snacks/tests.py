# from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class thingsTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

# run your test in the terminal by writing=>  python manage.py test