from django.db import models

class ProductClasses(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    classe = models.TextField()
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    classe = models.ForeignKey(
        ProductClasses, related_name="product", on_delete=models.CASCADE)

    def __str__(self):
        return self.name