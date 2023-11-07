from django.db import models
class ProductsData(models.Model):
    product_id=models.IntegerField()
    products_name=models.CharField(max_length=50)
    product_cost=models.IntegerField()
    product_description=models.CharField(max_length=50)