from django.db import models
from apps import model_choises as mch


class Standard(models.Model):
    title = models.SmallIntegerField(choices=mch.STANDARDS)
    steel = models.SmallIntegerField(choices=mch.STEEL)
    comment = models.TextField(max_length=15, blank=True, null=True)
    strength_yield = models.SmallIntegerField()
    strength_tensile = models.SmallIntegerField()
    extending = models.FloatField()

    #def __str__(self):
        #if self.title:
            #return f'{self.title} {self.steel}'


class Product(models.Model):
    # In Product model shs means structural hollow sections, and rp means round pipe
    width_shs = models.FloatField(null=True, blank=True)
    height_shs = models.FloatField(null=True, blank=True)
    diameter_pipe = models.FloatField(null=True, blank=True)
    wall = models.FloatField(null=False, blank=False)



    def __str__(self):
        if self.diameter_pipe is None:
            return f'{self.width_shs}x{self.height_shs}x{self.wall}'
        return f'{self.diameter_pipe}x{self.wall}'


class PurchaseInvoice(models.Model):
    act_date = models.DateField()
    act_number = models.SmallIntegerField()
    counterparty = models.TextField() # FK to Counterparties
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    standard = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.SET_NULL)
    length_from = models.PositiveSmallIntegerField(choices=mch.LENGTH)
    length_to = models.PositiveSmallIntegerField(choices=mch.LENGTH)
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
    base_units_weight = models.PositiveSmallIntegerField(choices=mch.UNITS)
    base_units_length = models.PositiveSmallIntegerField(choices=mch.UNITS)
    weight_acc = models.FloatField()
    weight_fact = models.FloatField()
    stock = models.TextField() # FK to stocks
    place = models.TextField() # FK to places
    contract = models.TextField() #FK to contracts
    created_by = models.TextField() # FK to staff_users
    create_date = models.DateField()

# TODO redef SAVE for this form! Length to must be => length from

