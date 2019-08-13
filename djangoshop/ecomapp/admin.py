from django.contrib import admin
from ecomapp.models import Category, Product,Production,ProductIMG
# Register your models here.

class ProductIMGInline(admin.StackedInline):
    model = ProductIMG
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductIMGInline,
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Production)
admin.site.register(ProductIMG)
