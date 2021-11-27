from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
import locale

locale.setlocale(locale.LC_ALL, 'en_US')
register = template.Library()

@register.filter()
def formatcurrency(value):
    return locale.currency(value, grouping=True)

@register.filter()
def percent(value):
    return format(value, ".2%")

@register.filter()
def iconimage(value):
    iconimagename = 'https://s2.coinmarketcap.com/static/img/coins/64x64/'+str(value) +'.png'
    return (iconimagename )

