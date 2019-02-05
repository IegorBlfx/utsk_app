from django.contrib import admin
from apps.account.models import TypeOfProduct, Steel, Standard, MechanicalProperties, Product, PurchaseInvoice

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product,ProductAdmin)

@admin.register(TypeOfProduct)
class TypeOfProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Steel)
class SteelAdmin(admin.ModelAdmin):
    pass

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    pass

@admin.register(MechanicalProperties)
class MechanicalPropertiesAdmin(admin.ModelAdmin):
    pass

@admin.register(PurchaseInvoice)
class PurchaseInvoiceAdmin(admin.ModelAdmin):
    pass