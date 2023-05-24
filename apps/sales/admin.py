from django.contrib import admin
from .models import Sale


class SaleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Date', {'fields': ('data',)}),
        ('Product', {'fields': ('product',)}),
        ('Quantity', {'fields': ('quantity',)}),
        ('Payment', {'fields': ('payment',)}),
    )
    list_filter = ['data', 'payment', 'product']
    list_display = ['product', 'quantity', 'payment']


admin.site.register(Sale, SaleAdmin)
