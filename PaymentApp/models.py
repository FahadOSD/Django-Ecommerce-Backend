from django.db import models
import uuid 
from accounts.models import Product

class PurchaseHistory(models.Model):

    purchase_id = models.CharField(max_length=225, default=uuid.uuid4())
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='product_tag')
    purchase_success = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)