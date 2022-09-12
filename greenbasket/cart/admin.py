from django.contrib import admin
from .models import CartItem


# admin.site.register(CartItem)

class CartItemAdmin(admin.ModelAdmin):

    list_display = ['user','product_name','product_price','product_quantity']

    def get_form(self, request, obj=None, **kwargs):
        form = super(CartItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].label_from_instance = lambda inst: "{} {}".format(inst.product_name, inst.product_price)
        return form


admin.site.register(CartItem, CartItemAdmin)

