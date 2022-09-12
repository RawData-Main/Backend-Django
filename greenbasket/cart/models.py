from urllib import request
from django.db import models
from django.contrib import admin
from product.models import ProductModel
from user.models import Customer
from django.conf import settings
from django.contrib.auth import get_user_model




        
class CartItem(models.Model):
    # current_user = request.user
    # u_id = current_user.id
    # user_id = Customer.objects.get(user_id = u_id)  
    # User = settings.AUTH_USER_MODEL
    User=get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # newly added. 
    product_name = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_name")
    product_price = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_price")
    product_quantity = models.PositiveIntegerField()

    # def __str__(self) -> str:
    #     return str(self.product_name)


    # def __str__(self):
    #     return f'{self.product_name} {self.product_price}'
    def __str__(self):
        return 'CartItem: {}'.format(self.product_name)