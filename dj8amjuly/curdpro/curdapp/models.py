from django.db import models
class ProductData(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    product_color = models.CharField(max_length=100)
    product_class = models.CharField(max_length=100)
    product_cost = models.IntegerField()
    number_of_items = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_mobile = models.BigIntegerField()
    customer_email = models.EmailField(max_length=100)