from django.contrib import admin
from apps.account.models import *

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product,ProductAdmin)

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    pass

@admin.register(PurchaseInvoice)
class PurchaseInvoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Counterparty)
class Counterparty(admin.ModelAdmin):
    pass

