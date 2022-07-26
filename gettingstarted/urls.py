from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

from hello.views import *

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", StockListView.as_view(), name="all"),
    path('stock/<int:pk>/detail', StockDetailView.as_view(), name='stock_detail'),
    path('stock/create/', StockCreateView.as_view(), name='stock_create'),
    path('stock/<int:pk>/update/', StockUpdateView.as_view(), name='stock_update'),
    path('stock/<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),
    
    path("admin/", admin.site.urls),
]

