from django.db import models
from django.contrib import admin
from product.models import ProductModel
from user.models import Customer


class CartItem(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) # newly added. 
    product_name = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_name")
    product_price = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_price")
    product_quantity = models.PositiveIntegerField()

    # def __str__(self) -> str:
    #     return str(self.product_name)


    # def __str__(self):
    #     return f'{self.product_name} {self.product_price}'

    # def __str__(self):
    #     temp = '{0.product_name} {0.product_price}'
    #     return temp.format(self) 
    # class CartAdmin(admin.ModelAdmin):
    #     list_display = ('name', 'price') 
    # class CartItemAdmin(admin.ModelAdmin):  
    #     list_display = ['user','product_name','product_price','product_quantity']

    #     def get_form(self, request, obj=None, **kwargs):
    #         form = super(self.CartItemAdmin, self).get_form(request, obj, **kwargs)
    #         form.base_fields['user'].label_from_instance = lambda inst: "{} {}".format(inst.product_name, inst.product_price)
    #         return form
    def __str__(self):
        return 'CartItem: {}'.format(self.product_name)