from django.test import TestCase


class onboardingTest(TestCase):
    def testHome(self):
        response = self.client.get('/onboarding/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'onboarding/onboarding.html', 'onboarding/liste.html')
        self.assertContains(response, '<h2 style="margin-top: 20px">Welcome to CIMD\'s onboarding wizard</h2>')

