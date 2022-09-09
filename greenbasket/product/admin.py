from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CategoryModel)

# admin.site.register(ProductModel)

class ProductItemAdmin(admin.ModelAdmin):

    list_display = ['name','price']

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProductItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['name'].label_from_instance = lambda inst: "{} {}".format(inst.name, inst.price)
        return form


admin.site.register(ProductModel, ProductItemAdmin)

admin.site.register(PlantModel)






