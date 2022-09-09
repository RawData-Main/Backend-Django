from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'category', views.CategoryModelViewSet)
router.register(r'product', views.ProductModelViewSet)
router.register(r'plant', views.PlantModelViewSet)




urlpatterns = [
    path('', include((router.urls, 'greenbasket.product'))),
]