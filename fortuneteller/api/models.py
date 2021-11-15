from django.db import models
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import datetime
import statsmodels.api as smt
import time
#stats models OLS tutorial https://www.geeksforgeeks.org/ordinary-least-squares-ols-using-statsmodels/
#Data analysis packages learned from DGMD S-14 Prof.Jose Ramirez Herran, Harvard Summer School

#Patch for dataframe to handle large numbers https://stackoverflow.com/questions/61732956/pandas-read-json-with-int64-values-raises-valueerror-value-is-too-big
pd.io.json._json.loads = lambda s, *a, **kw: json.loads(s)

class Test:
    # Set up default API values
    Price = "https://api.glassnode.com/v1/metrics/market/price_usd_close"
    Hashrate = "https://api.glassnode.com/v1/metrics/mining/hash_rate_mean"
    Accounts = "https://api.glassnode.com/v1/metrics/addresses/active_count"
    # Three tokens available
    Token = "ETH"  # BTC or ETH or LTC
    # Year start UNIX timestamps, represent January 1st
    Year_2021 = "1609459200"
    Year_2020 = "1577854800"
    Year_2019 = "1546300800"
    Year_2018 = "1514764800"
    Year_2017 = "1483228800"
    Year_2016 = "1451606400"
    # Choose your default start year
    Data_start_year = Year_2018
    # Choose your default frequency eg "1w" or "24h"
    Data_frequency = "24h"
    # Choose to log price data by base e
    Natural_log = False



# Create your models here.
