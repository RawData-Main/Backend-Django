from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django . dispatch import receiver
from django.conf import settings




# class ProfileModel(models.Model):
#     gender_choices = (
#         ("M","Male"),("F","Female"),("Others","Others")
#     )
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     gender = models.CharField(max_length=10,choices=gender_choices)
#     age = models.IntegerField(default=0)
#     address = models.CharField(max_length=100)
#     phone_no = models.CharField(max_length=14,default=0)
#     created_on = models.DateField(auto_now_add=True)
#     updated_on = models.DateField(auto_now=True)
#     status = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class User(AbstractUser):
    is_customer = models.BooleanField(default = False)
    is_report_user = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.username

@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created = False,**kwargs):
    if created:
        Token.objects.create(user = instance)



class Customer(models.Model):
    user = models.OneToOneField(User,related_name="customer",on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # def __str__(self):
    #     return self.user

class ReportUser(models.Model):
    user = models.OneToOneField(User,related_name="report_user",on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # def __str__(self):
    #     return self.user
    



