from django.contrib import admin
from apps.account.models import Standard, Product, PurchaseInvoice

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product,ProductAdmin)

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    pass

@admin.register(PurchaseInvoice)
class PurchaseInvoiceAdmin(admin.ModelAdmin):
    pass