from django.test import TestCase
from django.urls import reverse
from amir.models import Contact, NewsLetter


class ContactPageTests(TestCase):
    def test_contact_page_get(self):
        response = self.client.get(reverse('website:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_page_post_success(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Hello',
            'message': 'This is a test message'
        }
        response = self.client.post(reverse('website:contact'), data)
        self.assertRedirects(response, reverse('website:contact'))
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'Test User')
        self.assertEqual(contact.email, 'test@example.com')
        self.assertEqual(contact.subject, 'Hello')
        self.assertEqual(contact.message, 'This is a test message')

    def test_contact_page_post_invalid(self):
        # Missing required fields like message
        data = {
            'name': 'Test User',
            'email': 'invalid-email',
            'subject': 'Hello',
            'message': 'Some message'
        }
        response = self.client.post(reverse('website:contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 0)


class NewsLetterTests(TestCase):
    def test_newsletter_post_success(self):
        data = {
            'email': 'subscriber@example.com'
        }
        response = self.client.post(reverse('website:newsletter'), data)
        self.assertRedirects(response, '/')
        self.assertEqual(NewsLetter.objects.count(), 1)
        self.assertEqual(NewsLetter.objects.first().email, 'subscriber@example.com')

    def test_newsletter_post_invalid(self):
        data = {
            'email': 'invalid-email'
        }
        response = self.client.post(reverse('website:newsletter'), data)
        self.assertRedirects(response, '/')
        self.assertEqual(NewsLetter.objects.count(), 0)
