from django.db import models

# Model for workers in the pharmacy
class Staff(models.Model):
    names = models.CharField(max_length=100)
    phone_number= models.PositiveIntegerField()
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.names

# Model for the pharmacy's customers
class Customer(models.Model):
    names = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.names

# Pharmacy stock model
class Stock(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name