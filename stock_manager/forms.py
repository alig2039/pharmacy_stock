from django.contrib.auth.forms import UserCreationForm
from multiprocessing.connection import Client
from .models import *
from .views import *

class StockForm(models.Model):
    class Meta:
        model = Stock

class CustomerForm(models.Model):
    class Meta:
        model = Customer

class SalesForm(models.Model):
    class Meta:
        model = Sales
