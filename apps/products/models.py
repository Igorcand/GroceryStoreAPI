from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
