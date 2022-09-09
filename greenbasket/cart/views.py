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


# class CartItemViews(APIView):
#     queryset = CartItem.objects.all().order_by('id')

#     def post(self, request):
#         serializer = CartItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



#     def get(self, request, id=None):
#             if id:
#                 item = CartItem.objects.get(id=id)
#                 serializer = CartItemSerializer(item)
#                 return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

#             items = CartItem.objects.all()
#             serializer = CartItemSerializer(items, many=True)
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)     


#     def patch(self, request, id=None):
#         item = CartItem.objects.get(id=id)
#         serializer = CartItemSerializer(item, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})
#         else:
#             return Response({"status": "error", "data": serializer.errors})


#     def delete(self, request, id=None):
#         item = get_object_or_404(CartItem, id=id)
#         item.delete()
#         return Response({"status": "success", "data": "Item Deleted"})

##################################################


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all().order_by('id')
    serializer_class = CartItemSerializer

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


        ########### To decrease ordered item from stock ###########
        
        # for item in CartItem:
        #     ProductModel.objects.filter(id=item.id).first()
        #     ProductModel.stock = ProductModel.stock - item.product_quantity 
        #     ProductModel.save()
        #     CartItem.objects.filter(user=request.user).delete()
        


        return Response(status=status.HTTP_200_OK, data={'checkout_details': checkout_details})


        