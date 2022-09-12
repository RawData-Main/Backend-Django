from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CategoryModel)

# admin.site.register(ProductModel)
# admin.site.register(PlantModel)

class ProductItemAdmin(admin.ModelAdmin):

    list_display = ['name','price','stock','rating' ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProductItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['name'].label_from_instance = lambda inst: "{} {}".format(inst.name, inst.price, inst.stock, inst.rating)
        return form


admin.site.register(ProductModel, ProductItemAdmin)



class PlantItemAdmin(admin.ModelAdmin):

    list_display = ['plant_name','plant_type','propagation','plant_image','plant_desc']

    def get_form(self, request, obj=None, **kwargs):
        form = super(PlantItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['plant_name'].label_from_instance = lambda inst: "{} {}".format(inst.plant_name, inst.plant_type, inst.propagation, inst.plant_image, inst.plant_desc)
        return form


admin.site.register(PlantModel, PlantItemAdmin)





