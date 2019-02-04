from django.db import models

class TypeOfProduct(models.Model):
    product_type = models.TextField(unique=True, null=False, blank=False)

class Steel(models.Model):
    name = models.TextField(blank=False, null=False)

class Standard(models.Model):
    name = models.TextField(blank=False, null=False)
    number = models.TextField(blank=False, null=False)
    comment = models.TextField(blank=True, null=True)
    product_type = models.ForeignKey(TypeOfProduct, on_delete=models.SET_NULL(), related_name='standards')
    steel = models.ManyToManyField(Steel, on_delete=models.SET_NULL(), related_name='standards')

class MechanicalProperties(models.Model):
    strength_yield = models.SmallIntegerField()
    strength_tensile = models.SmallIntegerField()
    extending = models.FloatField()
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL(), related_name='properties')


class Product(models.Model):
    # In Product model shs means structural hollow sections, and rp means round pipe
    width_shs = models.FloatField(null=False, blank=True)
    height_shs = models.FloatField(null=False, blank=True)
    diameter_pipe = models.FloatField(null=False, blank=True)
    wall = models.FloatField(null=False, blank=False)
    product_type = models.ForeignKey(TypeOfProduct, on_delete=models.SET_NULL(), related_name='products')


