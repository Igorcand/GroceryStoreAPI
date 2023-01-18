from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.products.models import Product

# Create your models here.
PAYMENTS = (
        (u'0', u'Credit Card'),
        (u'1', u'Debit Card'),
        (u'2', u'Money'),
        )

class Sale(models.Model):
    data = models.DateField(null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                    MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    payment = models.CharField(
        max_length=3, null=True, blank=True, choices=PAYMENTS)
    
    def __str__(self):
        return f"{self.product} x {self.quantity}"