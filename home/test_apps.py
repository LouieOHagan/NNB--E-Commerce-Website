from django.test import TestCase
from .apps import HomeConfig


class TestApps(TestCase):

    def test_home_apps(self):
        self.assertEqual(HomeConfig.name, 'home')
