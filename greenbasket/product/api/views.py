
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from ..models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated

""" 

"""

class CategoryModelViewSet(viewsets.ModelViewSet):

    queryset = CategoryModel.objects.all().order_by('id')
    serializer_class = CategoryModelSerializer    
    authentication_classes = (TokenAuthentication, )


class ProductModelViewSet(viewsets.ModelViewSet):

    queryset = ProductModel.objects.all().order_by('id')
    serializer_class = ProductModelSerializer
    authentication_classes = (TokenAuthentication, )
   


class PlantModelViewSet(viewsets.ModelViewSet):

    queryset = PlantModel.objects.all().order_by('id')
    serializer_class = PlantModelSerializer  
    authentication_classes = (TokenAuthentication, )


