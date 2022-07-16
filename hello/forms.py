from multiprocessing.connection import Client
from .models import *
from .views import *

# Stock form
class StockForm(models.Model):
    class Meta:
        model = Stock

# Client form
class ClientForm(models.Model):
    class Meta:
        model = Client

# Staff form
class StaffForm(models.Model):
    class Meta:
        model = Staff