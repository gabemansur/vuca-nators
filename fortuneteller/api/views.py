from django.shortcuts import render
from django.http import HttpResponse
import requests
import time
import json

API_KEY = '20jIEsmDnwLuhZJSWzoDxZXmTq1'

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


