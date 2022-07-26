from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

class StockBaseView(View):
    model = Stock
    fields = '__all__'
    success_url = reverse_lazy('all')

class StockListView(StockBaseView, ListView):
    """View to list all stock.
    Use the 'stock_list' variable in the template
    to access all stock objects"""

class StockDetailView(StockBaseView, DetailView):
    """View to list the details from one stock.
    Use the 'stock' variable in the template to access
    the specific stock here and in the Views below"""

class StockCreateView(StockBaseView, CreateView):
    """View to create a new stock"""

class StockUpdateView(StockBaseView, UpdateView):
    """View to update a stock"""

class StockDeleteView(StockBaseView, DeleteView):
    """View to delete a stock"""



