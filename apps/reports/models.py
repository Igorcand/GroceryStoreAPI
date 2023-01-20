from django.db import models


class Reports(models.Model):
    product = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quantity_itens = models.IntegerField()
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=20)
    data = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Reports'

    def __str__(self):
        return f"{self.product} - {self.data}"
