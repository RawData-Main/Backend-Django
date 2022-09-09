from rest_framework import serializers
from ..models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','is_customer']


class ReportUserSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"},write_only = True)
    class Meta:
        model = User
        fields =['username','email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_report_user=True
        user.save()
        ReportUser.objects.create(user=user)
        return user







class CoustomerSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"},write_only = True)
    class Meta:
        model = User
        fields =['username','email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }


    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_customer=True
        user.save()
        Customer.objects.create(user=user)
        return user