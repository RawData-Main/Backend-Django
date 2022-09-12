from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from .models import CartItem
from product.models import ProductModel

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.decorators import action
from user.models import Customer
from .checkout_prepare import CartCheckout
from rest_framework.authentication import TokenAuthentication



class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all().order_by('id')
    serializer_class = CartItemSerializer
    # authentication_classes = (TokenAuthentication)

    @action(methods=['get'], detail=False, url_path='checkout/(?P<userId>[^/.]+)', url_name='checkout')
    def checkout(self, request, *args, **kwargs):

        try:
            user = Customer.objects.get(pk=int(kwargs.get('userId')))
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'Error': str(e)})

        cart_help = CartCheckout(user)
        checkout_details = cart_help.prepare_cart_for_checkout()

        if not checkout_details:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'error': 'Cart is empty !.'})

        return Response(status=status.HTTP_200_OK, data={'checkout_details': checkout_details})


        