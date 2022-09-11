from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Customer(models.Model):
    names = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.names

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                
                for field in self.__class__._meta.fields[1:]
            ]

class Supplier(models.Model):
    contact_name = models.CharField(max_length=100)
    supplier_name= models.CharField(max_length=100, default="Default")
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.contact_name

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))                
                for field in self.__class__._meta.fields[1:]
            ]

class Stock(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(1)])
    quantity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                
                for field in self.__class__._meta.fields[1:]
            ]

class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    drug = models.ForeignKey(Stock, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='updated_by')

    def __str__(self):
        return self.customer

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                
                for field in self.__class__._meta.fields[1:]
            ]

