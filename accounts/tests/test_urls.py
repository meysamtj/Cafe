from django.test import TestCase
from django.urls import resolve, reverse
from accounts.views import SignUpView


# Create your tests here.


class TestUrl(TestCase):
    def test_signupview(self):
        url = reverse('accounts:signup')
        self.assertEqual(resolve(url).func.view_class, SignUpView)
