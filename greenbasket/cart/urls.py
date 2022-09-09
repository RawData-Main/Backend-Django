from django.urls import path
# from .views import CartItemViews,CartViewSet
from .views import CartViewSet
from django.urls import include, path
from rest_framework import routers
from .checkout_prepare import CartCheckout


router = routers.DefaultRouter()

router.register(r'cart', CartViewSet, basename='cartitems')
# router.register(r'cart/checkout/', CartViewSet.checkout, basename='checkout')
# router.register(r'cart_items/', CartItemViews.as_view(), basename='cartitems')
# router.register(r'cart_items/<int:id>/', CartItemViews.as_view(), basename='cartitems_with_id')
# router.register(r'checkout/(?P<userId>[^/.]+)', CartViewSet, basename='checkout') #need clarifiction. .as_view , @action repeate inside view. 

#checkout path is inside views.py file. look for @action.

urlpatterns = [
    path('', include((router.urls, 'greenbasket.cart')))
]