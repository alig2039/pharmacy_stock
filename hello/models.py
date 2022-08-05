from django.db import models
from django.core.validators import MinValueValidator

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
    unit_price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                
                # if field.verbose_name != 'genre' 
                
                # else 
                #     (field.verbose_name, 
                #     Genre.objects.get(pk=field.value_from_object(self)).name)
                
                for field in self.__class__._meta.fields[1:]
            ]

class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    drug = models.ForeignKey(Stock, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.customer