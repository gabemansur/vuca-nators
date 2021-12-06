import json
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, response
from django.shortcuts import render
from django.urls import reverse
from .models import User, UserWatchlist

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def index(request):

    local_currency = 'USD'
    local_symbol = '$'
    api_key = 'fdccb806-f56e-46f5-88c6-8f45b3bd2c86'
    headers = {'X-CMC_PRO_API_KEY': api_key}
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=' + local_currency
    response = requests.get(url, headers=headers)
    results = response.json()
    data = results["data"]

    watchlist_arr = []
    if request.user.is_authenticated:
        try:
            # get watchlist by logged in user
            watchlist_arr = str(UserWatchlist.objects.get(user=request.user)).split(',')
        except UserWatchlist.DoesNotExist:
            # get or create watchlist by logged in user
            watchlist_arr = str(UserWatchlist.objects.get_or_create(user=request.user)).split(',')

    return render(request, "app/index.html", {'response': data, 'watchlist': watchlist_arr})


def watchlist(request):
    local_currency = 'USD'
    local_symbol = '$'
    api_key = 'fdccb806-f56e-46f5-88c6-8f45b3bd2c86'
    headers = {'X-CMC_PRO_API_KEY': api_key}
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=' + local_currency
    response = requests.get(url, headers=headers)
    results = response.json()
    data = results["data"]

    watchlist_arr = str(UserWatchlist.objects.get(user=request.user)).split(',')

    watchlist_data = []
    for crypto_object in data:
        if crypto_object["symbol"] in watchlist_arr:
            watchlist_data.append(crypto_object)


    return render(request, "app/watchlist.html", {'response': watchlist_data, 'watchlist': watchlist_arr})

@csrf_exempt
@login_required
def updatewatchlist(request):
    added = True
    if request.method == "POST":
        data = json.loads(request.body)
        symbol = data['symbol']

        # get watchlist by logged in user
        user_watchlist = UserWatchlist.objects.get(user=request.user)

        # convert user watchlist to array of symbols
        watchlist_arr = str(user_watchlist.watchlist).split(',')

        # check if symbol exists; true - remove, false - add
        if symbol in watchlist_arr:
            added = False
            watchlist_arr.remove(symbol)
        else:
            watchlist_arr.append(symbol)

        # array to string to prep for storing in db
        updated_watchlist_str = ",".join(watchlist_arr)

        # update user watchlist db object and save
        user_watchlist.watchlist = updated_watchlist_str
        user_watchlist.save()


    return JsonResponse({
        "updated_watchlist": updated_watchlist_str,
        "added": added
    }, safe=False)


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
   