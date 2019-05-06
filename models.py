from django.db import models
from django.utils.translation import ugettext_lazy as _


"""Our products available"""
class Product(models.Model):
    title = models.CharField(_('Title'), max_length=64, unique=True)

    def __str__(self):
        return self.title


"""The pricelists"""
class Pricelist(models.Model):
    title = models.CharField(_('Title'), max_length=64, unique=True)

    def __str__(self):
        return self.title


"""Assign products to priceslists"""
class PricelistProduct(models.Model):
    pricelist = models.ForeignKey(Pricelist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ("pricelist", "product")

    def __str__(self):
        return '{} - {}'.format(self.pricelist, self.product)
