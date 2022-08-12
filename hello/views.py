from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import *
from .models import *
from django.contrib.auth.models import User

class UserBaseView(View):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('whusers')

class UserListView(UserBaseView, ListView):
    """View to list all users.
    Use the 'user_list' variable in the template
    to access all users objects"""
    
class UserDetailView(UserBaseView, DetailView):
    """View to list the details from one users.
    Use the 'users' variable in the template to access
    the specific users here and in the Views below"""
    
class UserCreateView(PermissionRequiredMixin, UserBaseView, CreateView):
    """View to create a new users"""
    permission_required = 'users.add_user'

class UserUpdateView(PermissionRequiredMixin, UserBaseView, UpdateView):
    """View to update a stock"""
    permission_required = 'users.change_user'

class UserDeleteView(PermissionRequiredMixin, UserBaseView, DeleteView):
    """View to delete a stock"""
    permission_required = 'users.delete_user'

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

class StockCreateView(PermissionRequiredMixin, StockBaseView, CreateView):
    """View to create a new stock"""
    permission_required = 'stock.add_stock'

class StockUpdateView(PermissionRequiredMixin, StockBaseView, UpdateView):
    """View to update a stock"""
    permission_required = 'stock.change_stock'

class StockDeleteView(PermissionRequiredMixin, StockBaseView, DeleteView):
    """View to delete a stock"""
    permission_required = 'stock.delete_stock'

class CustomerBaseView(View):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customer')

class CustomerListView(CustomerBaseView, ListView):
    """View to list all stock.
    Use the 'customer_list' variable in the template
    to access all stock objects"""

class CustomerDetailView(CustomerBaseView, DetailView):
    """View to list the details from one Customer.
    Use the 'Customer' variable in the template to access
    the specific stock here and in the Views below"""

class CustomerCreateView(PermissionRequiredMixin, CustomerBaseView, CreateView):
    """View to create a new Customer"""
    permission_required = 'customer.add_customer'

class CustomerUpdateView(PermissionRequiredMixin, CustomerBaseView, UpdateView):
    """View to update a Customer"""
    permission_required = 'customer.change_customer'

class CustomerDeleteView(PermissionRequiredMixin, CustomerBaseView, DeleteView):
    """View to delete a Customer"""
    permission_required = 'customer.delete_customer'

class SalesBaseView(View):
    model = Sales
    fields = '__all__'
    success_url = reverse_lazy('sales')

class SalesListView(SalesBaseView, ListView):
    """View to list all SalesBaseView.
    Use the 'sales_list' variable in the template
    to access all Sales objects"""

class SalesDetailView(SalesBaseView, DetailView):
    """View to list the details from one sale.
    Use the 'Sales' variable in the template to access
    the specific Saleshere and in the Views below"""

class SalesCreateView(SalesBaseView, CreateView):
    """View to create a new sale"""
    def form_valid(self, form):
        self.object = form.save()
        #reduce stock from order number
        stock = Stock.objects.get(id=self.object.id)
        stock.quantity = stock.quantity - self.object.quantity
        stock.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())

class SalesUpdateView(SalesBaseView, UpdateView):
    """View to update a sale"""
    def form_valid(self, form):
        self.object = form.save()
        #reduce stock from order number
        #potential loop hole as update might deduct more as a total sale value
        stock = Stock.objects.get(id=self.object.id)
        stock.quantity = stock.quantity - self.object.quantity
        stock.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())


class SalesDeleteView(PermissionRequiredMixin, SalesBaseView, DeleteView):
    """View to delete a sale"""
    permission_required = 'sales.delete_sales' 

