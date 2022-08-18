from django.urls import path, include, re_path
from django.contrib import admin
admin.autodiscover()

from stock_manager.views import *

urlpatterns = [
    path("", StockListView.as_view(), name="all"),
    path('stock/<int:pk>/detail', StockDetailView.as_view(), name='stock_detail'),
    path('stock/create/', StockCreateView.as_view(), name='stock_create'),
    path('stock/<int:pk>/update/', StockUpdateView.as_view(), name='stock_update'),
    path('stock/<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),

    path('customer/', CustomerListView.as_view(), name='customer'),
    path('customer/<int:pk>/detail', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    path('sales/', SalesListView.as_view(), name='sales'),
    path('sales/<int:pk>/detail', SalesDetailView.as_view(), name='sales_detail'),
    path('sales/create/', SalesCreateView.as_view(), name='sales_create'),
    path('sales/<int:pk>/update/', SalesUpdateView.as_view(), name='sales_update'),
    path('sales/<int:pk>/delete/', SalesDeleteView.as_view(), name='sales_delete'),

    path('whusers/', UserListView.as_view(), name='whusers'),
    path('whusers/<int:pk>/detail', UserDetailView.as_view(), name='whusers_detail'),
    path('whusers/create/', UserCreateView.as_view(), name='whusers_create'),
    path('whusers/<int:pk>/update/', UserUpdateView.as_view(), name='whusers_update'),
    path('whusers/<int:pk>/delete/', UserDeleteView.as_view(), name='whusers_delete'),

    path("admin/", admin.site.urls),
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^register/", register, name="register"),

 
]

handler403 = 'stock_manager.views.permission_denied'
