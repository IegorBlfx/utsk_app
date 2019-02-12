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
class CounterpartyAdmin(admin.ModelAdmin):
    pass

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass
