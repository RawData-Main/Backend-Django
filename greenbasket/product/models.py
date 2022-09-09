from django.db import models
# from django.contrib.auth.models import User
from user.models import User
from greenbasket import settings

# Create your models here.

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=120)
    category_image = models.ImageField(null = True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.category_name


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    cost = models.FloatField()
    stock = models.IntegerField()###
    image = models.ImageField()
    description = models.TextField(max_length=200,blank=True, null=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.SET_NULL,null=True,blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    rating = models.FloatField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.CASCADE)

    # def __repr__(self):
    #     return (self.name, realted_name='name'),, self.price

    # def __str__(self):
    #     temp = '{0.name} {0.price}'
    #     return temp.format(self)    
       

    # def __str__(self):
    #     return f'{self.name},{self.price}'

    # def __str__(self):
    #     return  ({'name': self.name, 'price': self.price})

    # def __repr__(self):
    #     rep = '(' +  + ',' + str(self.price) + ')'
    #     return rep
    # def __str__(self):
    #     return 'ProductModel: {}'.format(self.name, self.price)

class PlantModel(models.Model):
    plant_name = models.ForeignKey(ProductModel,on_delete=models.CASCADE, related_name='plant_name')
    type = models.CharField(max_length=60)
    propagation = models.CharField(max_length=60)
    plant_image = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name='plant_image')
    plant_desc = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name='plant_desc')