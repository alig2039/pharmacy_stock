from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.urls import reverse

from .views import *
from .models import *


class CustomerTest(TestCase):
    #model tests
    def create_customer(self, names="test customer", address="test address", phone_number="12345"):
        return Customer.objects.create(names=names, address=address, phone_number=phone_number)

    def test_customer_creation(self):
        c = self.create_customer()
        self.assertTrue(isinstance(c, Customer))
        self.assertEqual(c.__str__(), c.names)

    # view tests
    def test_customer_list_view(self):
        url = reverse("customer")
        resp = self.client.get(url)
        if resp.status_code == '200':
            self.assertEqual(resp.status_code, 200)
        else:
            self.assertEqual(resp.status_code, 302)

    def test_customer_create_view(self):
        url = reverse("customer_create")
        resp = self.client.get(url)
        if resp.status_code == '200':
            self.assertEqual(resp.status_code, 200)
        else:
            self.assertEqual(resp.status_code, 302)

class SupplierTest(TestCase):
    #model tests
    def create_supplier(self, contact_name="test contact", supplier_name="test supplier",address="test address", contact_number="12345"):
        return Supplier.objects.create(contact_name=contact_name, supplier_name=supplier_name ,address=address, contact_number=contact_number)

    # view tests
    def test_supplier_list_view(self):
        url = reverse("supplier")
        resp = self.client.get(url)
        if resp.status_code == '200':
            self.assertEqual(resp.status_code, 200)
        else:
            self.assertEqual(resp.status_code, 302)

    def test_supplier_create_view(self):
        url = reverse("supplier_create")
        resp = self.client.get(url)
        if resp.status_code == '200':
            self.assertEqual(resp.status_code, 200)
        else:
            self.assertEqual(resp.status_code, 302)




# class SimpleTest(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()

#     def test_details(self):
#         # Create an instance of a GET request.
#         request = self.factory.get("/")
#         request.user = AnonymousUser()

#         # Test my_view() as if it were deployed at /customer/details
#         response = custom_login(request)
#         self.assertEqual(response.status_code, 200)
