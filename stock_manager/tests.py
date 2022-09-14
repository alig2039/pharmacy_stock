from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, SimpleTestCase
from django.urls import reverse

from .views import *
from gettingstarted.urls import urlpatterns

class UrlTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        for url in ["/", "/stock/create/", "/customer/", "/customer/create", "/sales/", "/sales/
create", "/supplier/create", "/supplier/", 
        "/whusers/create", "/whusers/"]:
            response = self.client.get(url)
            try:
                self.assertEqual(response.status_code, 301)
            except:
                self.assertEqual(response.status_code, 302)

    def test_url_available_by_name(self):
        for name in ["all", "stock_create", "customer", "customer_create", "sales", "sales_create", "supplier_create",
 "supplier", 
        "whusers_create", "whusers"]:
            response = self.client.get(reverse(name))
            try:
                self.assertEqual(response.status_code, 301)
            except:
                self.assertEqual(response.status_code, 302)

    # def test_template_name_correct(self):  
    #     response = self.client.get(reverse("home"))
    #     self.assertTemplateUsed(response, "pages/home.html")
