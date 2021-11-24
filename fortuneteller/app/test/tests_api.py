from django.test import TestCase
import unittest
import time

API_KEY = '20jIEsmDnwLuhZJSWzoDxZXmTq1'
ticker = 'BTC'

# Create your tests here.
#testing may need to be moved to tests.py to be cleaner
class MyTestCase(unittest.TestCase):
    def test_default(self):
        self.assertEqual(True, True)  # add assertion here

    def test_ticker(self):
        expected = 'BTC'
        actual = ticker
        self.assertEqual(expected, actual)

    def test_get_time_now(self):
        expected = round(time.time())
        actual = int(round(time.time()))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()