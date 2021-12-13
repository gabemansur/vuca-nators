from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")

@given(u'I am going to Fortune Teller website')
def step_impl(context):
    print('I am going to Fortune Teller website')

@when(u'I click on Register Menu option')
def step_impl(context):
    print('I click on Register Menu option')

@then(u'A registration form display')
def step_impl(context):
   print('A registration form display')

@then(u'I type the information and register a new user')
def step_impl(context):
    print('I type the information and register a new user')
