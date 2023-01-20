from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product', {
            'fields': ('name', 'description')
            }),
        ('Stock', {
            'fields': ('stock',)
            }),
        ('Price', {
            'fields': ('price',)
            }),
        ('Category', {
            'fields': ('category',)
            })
    )
    list_filter = ['category', 'price']
    list_display = ['name', 'stock', 'price']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Category', {
            'fields': ('name',)
            }),
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
