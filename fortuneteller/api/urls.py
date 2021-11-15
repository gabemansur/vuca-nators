from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('test', views.test, name='test'),
    path('get-price', views.getPrice, name='get price')
]