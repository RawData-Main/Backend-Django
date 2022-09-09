
# from rest_framework.views import APIView
# from rest_framework import viewsets
# from rest_framework.response import Response
# from .serializers import *
# from rest_framework.throttling import UserRateThrottle
# from ..models import *

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from ..models import *
from .serializers import *





class CategoryModelViewSet(viewsets.ModelViewSet):

    queryset = CategoryModel.objects.all().order_by('id')
    serializer_class = CategoryModelSerializer    


class ProductModelViewSet(viewsets.ModelViewSet):

    queryset = ProductModel.objects.all().order_by('id')
    serializer_class = ProductModelSerializer


class PlantModelViewSet(viewsets.ModelViewSet):

    queryset = PlantModel.objects.all().order_by('id')
    serializer_class = PlantModelSerializer  


