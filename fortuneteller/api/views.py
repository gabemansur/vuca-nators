from django.shortcuts import render
from django.http import HttpResponse
import requests
import time
import json
#testing may need to be moved to tests.py to be cleaner
import unittest

API_KEY = '20jIEsmDnwLuhZJSWzoDxZXmTq1'
ticker = 'BTC'

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world. You're in the api app.")

def test(request):
    url = 'https://api.glassnode.com/v1/metrics/market/price_usd_close'
    params = {'a': 'BTC', 'api_key': API_KEY}
    response = requests.get(url, params)
    return HttpResponse(response)

def getPrice(ticker):
    ticker = 'BTC'
    data_start_timestamp = round(time.time()) - 2629743 # minus 1 month
    data_end = round(time.time())
    data_frequency = '1w'
    url = 'https://api.glassnode.com/v1/metrics/market/price_usd_close'
    params = {'a': ticker, 'api_key': API_KEY, 's': data_start_timestamp, 'u': data_end, 'i': data_frequency}
    response = requests.get(url, params).json()

    return HttpResponse(response[-1]['v'] - response[-2]['v'])


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
