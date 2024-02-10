from django.db import models

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    depth = models.DecimalField(max_digits=6, decimal_places=2)
    material = models.CharField(max_length=254)
    colour = models.CharField(max_length=254, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='pic', null=True, blank=True)

    def _str_(self):
        return self.name
