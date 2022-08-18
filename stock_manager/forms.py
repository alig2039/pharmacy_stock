from django.contrib.auth.forms import UserCreationForm
from multiprocessing.connection import Client
from .models import *
from .views import *

# Stock form
class StockForm(models.Model):
    class Meta:
        model = Stock

# Client form
class CustomerForm(models.Model):
    class Meta:
        model = Customer

# Staff form
class SalesForm(models.Model):
    class Meta:
        model = Sales
