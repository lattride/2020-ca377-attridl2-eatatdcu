from django.test import TestCase
from django.urls import reverse

class A0Tests(TestCase):

    def test_welcome(self):
      """
      The index page loads and an appropriate welcome message is displayed
      """
      response = self.client.get(reverse('eatatdcu:index'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "Eat at DCU!")

    def test_restaurants(self):
      """
      The restaurants page loads and an appropriate message is displayed
      """
      response = self.client.get(reverse('eatatdcu:restaurants'))
      self.assertEqual(response.status_code, 200)

