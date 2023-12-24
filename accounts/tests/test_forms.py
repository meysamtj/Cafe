from django.test import TestCase
from accounts.models import CustomerUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


# from model_bakery import baker


class FormsTest(TestCase):
    def test_exist_email(self):
        CustomerUser.objects.create_user(username='meysamtajik', email='meysam@gmail.com', password='meysam123')
        form = CustomUserCreationForm(data={
            'username': 'meysam',
            'first_name': 'meysam',
            'last_name': 'meysam',
            'phone_number': '09389975502',
            'city': 'teh',
            'address': 'teh',
            'img': 'img/about.jpg',
            'email': 'meysam@gmail.com',
            'password1': 'meyWDFSCXsam@$%@!RE#123',
            'password2': 'meyWDFSCXsam@$%@!RE#123'

        })
        print('errors:', form.errors)
        self.assertEqual(len(form.errors), 0)
        self.assertFalse(form.has_error('email'))
