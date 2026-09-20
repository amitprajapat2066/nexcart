from django.contrib import admin
from .models import Product, Category, Order


admin.site.register(Product)
admin.site.register(Category)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'mobile',
        'city',
        'pincode',
        'created_at',
    )