from django.db import models

class TypeOfProduct(models.Model):
    product_type = models.TextField(max_length=20 ,unique=True, null=True, blank=False)

    def __str__(self):
        return self.product_type

class Steel(models.Model):
    name = models.TextField(max_length=15 ,blank=False, null=False)

    def __str__(self):
        return self.name

class Standard(models.Model):
    name = models.TextField(max_length=15, blank=False, null=False)
    number = models.TextField(max_length=15, blank=False, null=False)
    comment = models.TextField(max_length=15, blank=True, null=True)
    product_type = models.ForeignKey(TypeOfProduct, null=True, blank=True, on_delete=models.SET_NULL, related_name='standards')
    steel = models.ManyToManyField(Steel)

    def __str__(self):
        return self.name

class MechanicalProperties(models.Model):
    strength_yield = models.SmallIntegerField()
    strength_tensile = models.SmallIntegerField()
    extending = models.FloatField()
    standard = models.ForeignKey(Standard, null=True, on_delete=models.SET_NULL, related_name='properties')

    def __str__(self):
        return self.standard

class Product(models.Model):
    # In Product model shs means structural hollow sections, and rp means round pipe
    width_shs = models.FloatField(null=True, blank=True)
    height_shs = models.FloatField(null=True, blank=True)
    diameter_pipe = models.FloatField(null=True, blank=True)
    wall = models.FloatField(null=False, blank=False)
    product_type = models.ForeignKey(TypeOfProduct, null=True, on_delete=models.SET_NULL, related_name='products')

#class Length(models.Model):
    #length = models.FloatField(null=True, blank=True)

#class BaseUnits(models.Model):
    #base_units = models.TextField(max_length=10)

class PurchaseInvoice(models.Model):
    act_date = models.DateField()
    act_number = models.SmallIntegerField()
    counterparty = models.TextField() # FK to Counterparties
    standard = models.ForeignKey(Standard, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    steel = models.ForeignKey(Steel, null=True, blank=True, on_delete=models.SET_NULL)
    length_from = models.FloatField()#ForeignKey(Length, null=True, blank=True, on_delete=models.SET_NULL)
    length_to = models.FloatField() #ForeignKey(Length, null=True, blank=True, on_delete=models.SET_NULL)
    wall_thickness_max = models.FloatField()
    wall_thickness_min = models.FloatField()
    radius_rounding_max = models.FloatField()
    radius_rounding_min = models.FloatField()
    pipe_diam_out = models.FloatField()
    pipe_diam_in = models.FloatField()
    uktzed = models.IntegerField() #FK uktzed
    price_in = models.FloatField() # must be in document
    price_in_nds = models.FloatField() # must be in document
    price_out = models.FloatField()
    price_out_NDS = models. FloatField()
    base_units_weight = models.TextField()#ForeignKey(BaseUnits, null=True, blank=True, on_delete=models.SET_NULL)
    base_units_length = models.TextField()#ForeignKey(BaseUnits, null=True, blank=True, on_delete=models.SET_NULL)
    weight_acc = models.FloatField()
    weight_fact = models.FloatField()
    stock = models.TextField() # FK to stocks
    place = models.TextField() # FK to places
    contract = models.TextField() #FK to contracts
    created_by = models.TextField() # FK to staff_users
    create_date = models.DateField()




