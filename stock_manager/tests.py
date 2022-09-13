from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, SimpleTestCase
from django.urls import reverse

from .views import *
from gettingstarted.urls import urlpatterns

