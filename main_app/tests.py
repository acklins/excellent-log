from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse

# Create your tests here.
#checking that the url I defined in urls.py works
class HomePageTests(SimpleTestCase):
    def test_home_url_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
