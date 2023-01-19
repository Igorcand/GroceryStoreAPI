from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.products.models import Product

# Create your models here.
PAYMENTS = (
    ("0", "Credit Card"),
    ("1", "Debit Card"),
    ("2", "Money"),
)


class Sale(models.Model):
    class PaymentsType(models.TextChoices):
        CREDIT_CARD = "Credit Card"
        DEBIT_CARD = "Debit Card"
        MONEY = "Money"

    data = models.DateField(null=True, blank=True)
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL
    )
    quantity = models.DecimalField(
        max_digits=13,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        null=True,
        blank=True,
    )
    payment = models.CharField(max_length=30, null=True, blank=True,  choices=PaymentsType.choices, default=PaymentsType.CREDIT_CARD)

    def __str__(self):
        return f"{self.product} x {self.quantity}"
