import json
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, response
from django.shortcuts import render
from django.urls import reverse
from .models import User

def index(request):
    return render(request, "app/index.html", {})

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "app/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "app/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def cripton_market(request):
    local_currency ='USD'
    local_symbol = '$'
    api_key = 'fdccb806-f56e-46f5-88c6-8f45b3bd2c86'
    headers = {'X-CMC_PRO_API_KEY': api_key}
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=' + local_currency
    response =requests.get(url, headers=headers)
    results = response.json()
    data = results["data"]
    """  for currency in data:
        name = currency['name']
        symbol = currency['symbol']

        price = currency['quote'][local_currency]['price']
        market_cap = round(currency['quote'][local_currency]['market_cap'],2)
        percent_change_24h = round(currency['quote'][local_currency]['percent_change_24h'],2)
        circulating_supply = round(currency['circulating_supply'],2)
        volume_24h =round(currency['quote'][local_currency]['volume_24h'],2)
        volume_change_24h = round(currency['quote'][local_currency]['volume_change_24h'],2)

        price = round(price,2)
        price_string = local_symbol + '{:,}'.format(price)
        market_cap_string = local_symbol + '{:,}'.format(market_cap)
        circulating_supply_string = local_symbol + '{:,}'.format(circulating_supply)
        volume_24h_string = local_symbol + '{:,}'.format(volume_24h)
        volume_change_24h_string = local_symbol + '{:,}'.format(volume_change_24h)

        print(name +'('+ symbol +')')
        print('Price  :' +price_string)
        print('Market_cap :' + market_cap_string)
        print('Circulate 24 :' +circulating_supply_string)
        print('volume 24h :'+volume_24h_string)
        print('volume change :'+ volume_change_24h_string)   """   
    return render(request,'app/criptonmarket.html',{'response':data})
   
