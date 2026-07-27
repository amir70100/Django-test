from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class SignupViewTests(TestCase):
    def test_signup_creates_and_logs_in_user(self):
        response = self.client.post(reverse('account:signup_view'), {
            'username': 'amir',
            'first_name': 'Amir',
            'last_name': 'Ahmadi',
            'email': 'amir@example.com',
            'password1': 'Secure-password-123',
            'password2': 'Secure-password-123',
        })

        self.assertRedirects(response, '/')
        user = User.objects.get(username='amir')
        self.assertEqual(user.email, 'amir@example.com')
        self.assertEqual(self.client.session['_auth_user_id'], str(user.pk))
