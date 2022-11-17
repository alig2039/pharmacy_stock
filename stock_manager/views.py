from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import *
from django.template import RequestContext
from .models import *

def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('all'))
    else:
        return login(request)


class UserBaseView(View):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('whusers')

class UserListView(UserBaseView, ListView):
    pass
    
class UserDetailView(UserBaseView, DetailView):
    pass
    
class UserCreateView(PermissionRequiredMixin, UserBaseView, CreateView):
    permission_required = 'auth.add_user'

class UserUpdateView(PermissionRequiredMixin, UserBaseView, UpdateView):
    permission_required = 'auth.change_user'

class UserDeleteView(PermissionRequiredMixin, UserBaseView, DeleteView):
    permission_required = 'auth.delete_user'

class StockBaseView(View):
    model = Stock
    fields = '__all__'
    success_url = reverse_lazy('all')

class StockListView(StockBaseView, ListView):
    pass
    
class StockDetailView(StockBaseView, DetailView):
    pass
    
class StockCreateView(PermissionRequiredMixin, StockBaseView, CreateView):
    permission_required = 'stock.add_stock'

class StockUpdateView(PermissionRequiredMixin, StockBaseView, UpdateView):
    permission_required = 'stock.change_stock'

class StockDeleteView(PermissionRequiredMixin, StockBaseView, DeleteView):
    permission_required = 'stock.delete_stock'

class CustomerBaseView(View):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customer')

class CustomerListView(CustomerBaseView, ListView):
    pass
    
class CustomerDetailView(CustomerBaseView, DetailView):
    pass
    
class CustomerCreateView(PermissionRequiredMixin, CustomerBaseView, CreateView):
    permission_required = 'customer.add_customer'

class CustomerUpdateView(PermissionRequiredMixin, CustomerBaseView, UpdateView):
    permission_required = 'customer.change_customer'

class CustomerDeleteView(PermissionRequiredMixin, CustomerBaseView, DeleteView):
    permission_required = 'customer.delete_customer'

class SupplierBaseView(View):
    model = Supplier
    fields = '__all__'
    success_url = reverse_lazy('supplier')

class SupplierListView(SupplierBaseView, ListView):
    pass
    
class SupplierDetailView(SupplierBaseView, DetailView):
    pass
    
class SupplierCreateView(PermissionRequiredMixin, SupplierBaseView, CreateView):
    permission_required = 'supplier.add_supplier'

class SupplierUpdateView(PermissionRequiredMixin, SupplierBaseView, UpdateView):
    permission_required = 'supplier.change_supplier'

class SupplierDeleteView(PermissionRequiredMixin, SupplierBaseView, DeleteView):
    permission_required = 'supplier.delete_supplier'

class SalesBaseView(View):
    model = Sales
    fields = '__all__'
    success_url = reverse_lazy('sales')

class SalesListView(SalesBaseView, ListView):
    pass
    
class SalesDetailView(SalesBaseView, DetailView):
    pass
    
class SalesCreateView(SalesBaseView, CreateView):
    fields = ['customer', 'drug', 'quantity']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        self.object = form.save()
        #reduce stock from order number
        stock = Stock.objects.get(name=self.object.drug)
        stock.quantity = stock.quantity - self.object.quantity
        stock.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())

class SalesUpdateView(SalesBaseView, UpdateView):
    fields = ['customer', 'drug', 'quantity']

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        self.object = form.save()
        #reduce stock from order number
        #potential loop hole as update might deduct more as a total sale value
        stock = Stock.objects.get(name=self.object.drug)
        stock.quantity = stock.quantity - self.object.quantity
        stock.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())

class SalesDeleteView(PermissionRequiredMixin, SalesBaseView, DeleteView):
    permission_required = 'sales.delete_sales' 

def register(request):
    if request.method == "GET":
        return render(
            request, "stock_manager/register.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('whusers'))
        else:
            return render(
            request, "stock_manager/register.html",
            {"form": UserCreationForm}
        )

def permission_denied(request, exception):
   context = {}
   return render(request,'errors/403.html', context)