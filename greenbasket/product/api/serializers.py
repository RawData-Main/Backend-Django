from rest_framework import serializers
from product.models import *
from .serializers import *



class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"        

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

class PlantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantModel
        fields = "__all__"        
