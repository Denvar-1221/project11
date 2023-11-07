from django.contrib import admin
from .models import ProductsData
class AdminProductsData(admin.ModelAdmin):
    list_display=['product_id','product_name','product_cost','product_description']
admin.site.register(ProductsData,AdminProductsData)


# Register your models here.
