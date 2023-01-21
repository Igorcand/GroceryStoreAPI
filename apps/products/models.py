from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    class UnitType(models.TextChoices):
        ITEM = "Item"
        KG = "Kg"

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    stock = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        choices=UnitType.choices,
        default=UnitType.ITEM,
    )
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
