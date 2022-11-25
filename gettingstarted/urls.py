from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

from stock_manager.views import *
from stock_manager.forms import *

urlpatterns = [
    path("", login_required(StockListView.as_view()), name="all"),
    path('stock/<int:pk>/detail', login_required(StockDetailView.as_view()), name='stock_detail'),
    path('stock/create/', login_required(StockCreateView.as_view()), name='stock_create'),
    path('stock/<int:pk>/update/', login_required(StockUpdateView.as_view()), name='stock_update'),
    path('stock/<int:pk>/delete/', login_required(StockDeleteView.as_view()), name='stock_delete'),

    path('customer/', login_required(CustomerListView.as_view()), name='customer'),
    path('customer/<int:pk>/detail', login_required(CustomerDetailView.as_view()), name='customer_detail'),
    path('customer/create/', login_required(CustomerCreateView.as_view()), name='customer_create'),
    path('customer/<int:pk>/update/', login_required(CustomerUpdateView.as_view()), name='customer_update'),
    path('customer/<int:pk>/delete/', login_required(CustomerDeleteView.as_view()), name='customer_delete'),

    path('sales/', login_required(SalesListView.as_view()), name='sales'),
    path('sales/<int:pk>/detail', login_required(SalesDetailView.as_view()), name='sales_detail'),
    path('sales/create/', login_required(SalesCreateView.as_view()), name='sales_create'),
    path('sales/<int:pk>/update/', login_required(SalesUpdateView.as_view()), name='sales_update'),
    path('sales/<int:pk>/delete/', login_required(SalesDeleteView.as_view()), name='sales_delete'),

    path('supplier/', login_required(SupplierListView.as_view()), name='supplier'),
    path('supplier/<int:pk>/detail', login_required(SupplierDetailView.as_view()), name='supplier_detail'),
    path('supplier/create/', login_required(SupplierCreateView.as_view()), name='supplier_create'),
    path('supplier/<int:pk>/update/', login_required(SupplierUpdateView.as_view()), name='supplier_update'),
    path('supplier/<int:pk>/delete/', login_required(SupplierDeleteView.as_view()), name='supplier_delete'),

    path('whusers/', login_required(UserListView.as_view()), name='whusers'),
    path('whusers/<int:pk>/detail', login_required(UserDetailView.as_view()), name='whusers_detail'),
    path('whusers/create/', login_required(UserCreateView.as_view()), name='whusers_create'),
    path('whusers/<int:pk>/update/', login_required(UserUpdateView.as_view()), name='whusers_update'),
    path('whusers/<int:pk>/delete/', login_required(UserDeleteView.as_view()), name='whusers_delete'),

    path('login', custom_login, name = 'login '),

    path("admin/", admin.site.urls),
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^register/", register, name="register"), 
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler403 = 'stock_manager.views.permission_denied'
