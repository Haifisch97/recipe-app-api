"""
Sample test
"""
from django.test import SimpleTestCase


class CalcTests(SimpleTestCase):
    """Sample test class"""

    def test_always_passes(self):
        self.assertEqual(1, 1)
