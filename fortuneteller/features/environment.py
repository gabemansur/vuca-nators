import os
import django
from behave.runner import Context
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.management import call_command
from django.shortcuts import resolve_url
from django.test.runner import DiscoverRunner
from splinter.browser import Browser

#def before_all(context):
   # context.browser = Browser('chrome', headless=True)

#def after_all(context):
    #context.browser.quit()
    #context.browser = None