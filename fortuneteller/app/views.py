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
    api_key = 'fdccb806-f56e-46f5-88c6-8f45b3bd2c86'
    headers = {'X-CMC_PRO_API_KEY': api_key}
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=' + local_currency
    response =requests.get(url, headers=headers)
    results = response.json()
    data = results["data"]
    print(json.dumps(results, sort_keys=True, indent=4))
    #print(json.dumps(data, sort_keys=True, indent=4))
    return render(request,'app/criptonmarket.html',{'response':results})
