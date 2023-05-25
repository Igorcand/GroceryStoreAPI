from django.contrib import admin

from .models import Reports


class ReportAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product', {'fields': ('product', 'category')}),
        ('Quantity', {'fields': ('quantity_itens',)}),
        ('Payment', {'fields': ('payment',)}),
        ('Date', {'fields': ('data',)}),
    )
    list_filter = ['data', 'product', 'category', 'payment']
    list_display = ['product', 'quantity_itens', 'payment', 'sale']


admin.site.register(Reports, ReportAdmin)
