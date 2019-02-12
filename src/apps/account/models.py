from django.db import models
from apps import model_choises as mch


class Location(models.Model):
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.country} ,{self.region} ,{self.city} ,{self.street}'

class Place(models.Model):
    stock = models.CharField(max_length=50)
    playground = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.place} ,{self.playground} ,{self.stock}'

class Counterparty(models.Model):
    ownership_type = models.SmallIntegerField(choices=mch.OWNERSHIP)
    name = models.CharField(max_length=120)
    inn = models.IntegerField()
    edrpou = models.IntegerField()
    country = models.ForeignKey(Location, null=True,blank=True, on_delete=models.SET_NULL)
    adress_by_documents = models.CharField(max_length=200) #TODO separate this field on 3 different
    adress_by_fact = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    create_by = models.CharField(max_length=50) # TODO create user_is_staff class


class Contract(models.Model):
    created_date = models.DateField()
    contract_type = models.SmallIntegerField(choices=mch.CONTRACT)
    contract_number = models.CharField(max_length=15)
    counterparty = models.ForeignKey(Counterparty,null=True,blank=True, on_delete=models.SET_NULL)
    our_company = models.SmallIntegerField(choices=mch.COMPANY) # TODO take it from second DB
    type_nds = models.SmallIntegerField(choices=mch.NDS) # TODO take it from second DB
    contract_currency = models.SmallIntegerField(choices=mch.CURRENCY)
    contract_from = models.DateField()
    contract_to = models.DateField()
    contract_amount = models.FloatField()
    created_by = models.CharField(max_length=15) # TODO user_is_staff

    def __str__(self):
        return f'{self.get_contract_type_display} contract #{self.contract_number}'

class Document(models.Model):
    title = models.CharField(max_length=15)
    doc_date = models.DateField()
    doc_number = models.CharField(max_length=15)
    contract = models.ForeignKey(Contract, null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.CharField(max_length=15)
    created_date = models.DateField()

class Standard(models.Model):
    title = models.SmallIntegerField(choices=mch.STANDARDS)
    steel = models.SmallIntegerField(choices=mch.STEEL)
    comment = models.TextField(max_length=15, blank=True, null=True)
    strength_yield = models.SmallIntegerField()
    strength_tensile = models.SmallIntegerField()
    extending = models.FloatField()

    def __str__(self):
        if self.title:
            return f'{self.get_title_display()} {self.get_steel_display()}'


class Product(models.Model):
    # In Product model shs means structural hollow sections, and rp means round pipe
    width_shs = models.FloatField(null=True, blank=True)
    height_shs = models.FloatField(null=True, blank=True)
    diameter_pipe = models.FloatField(null=True, blank=True)
    wall = models.FloatField(null=False, blank=False)



    def __str__(self):
        if self.diameter_pipe is None:
            return f'{self.width_shs} x {self.height_shs} x {self.wall}'
        return f'{self.diameter_pipe} x {self.wall}'


class PurchaseInvoice(models.Model):
    document = models.ForeignKey(Document, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    standard = models.ForeignKey(Standard, blank=True, null=True, on_delete=models.SET_NULL)
    length_from = models.PositiveSmallIntegerField(choices=mch.LENGTH)
    length_to = models.PositiveSmallIntegerField(choices=mch.LENGTH)
    wall_thickness_max = models.FloatField(null=True, blank=True)
    wall_thickness_min = models.FloatField(null=True, blank=True)
    radius_rounding_max = models.FloatField(null=True, blank=True)
    radius_rounding_min = models.FloatField(null=True, blank=True)
    pipe_diam_out = models.FloatField(null=True, blank=True)
    pipe_diam_in = models.FloatField(null=True, blank=True)
    uktzed = models.IntegerField(null=True, blank=True) #FK uktzed
    price_in = models.FloatField(null=True, blank=True) # must be in document
    price_in_nds = models.FloatField(null=True, blank=True) # must be in document
    price_out = models.FloatField(null=True, blank=True)
    price_out_NDS = models. FloatField(null=True, blank=True)
    base_units_weight = models.PositiveSmallIntegerField(choices=mch.UNITS)
    base_units_length = models.PositiveSmallIntegerField(choices=mch.UNITS)
    weight_acc = models.FloatField(null=True, blank=True)
    weight_fact = models.FloatField(null=True, blank=True)
    stock = models.TextField(null=True, blank=True) # TODO FK to stocks, def function GetStock
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.SET_NULL)


# TODO redef SAVE for this form! Length to must be => length from





