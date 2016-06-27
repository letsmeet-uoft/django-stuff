from django.test import TestCase

# Create your tests here.

class UserProfileTesting(TestCase):
	def setup(self):
		UserProfile.objects.create()


	def test_delete(self):

