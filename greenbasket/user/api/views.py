from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import *
from django.http import request
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsReportUser, IsCustomerUser
from django.contrib.auth import logout
from django.views.generic import View
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

 



class ReportUserSignupView(generics.GenericAPIView):
    serializer_class = ReportUserSignupSerializer
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })


class CustomerSignupView(generics.GenericAPIView):
    serializer_class=CoustomerSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_report_user':user.is_report_user,
            'is_customer':user.is_customer
        })
    


#--------------------LOGOUT----------------------#

class LogoutView(GenericAPIView):
    def get(self, request, format=None):
            # simply delete the token to force a login
            if request.user.is_authenticated:
                request.user.auth_token.delete()
            if request.user.is_authenticated:
                print("logout failed")
            else:
                print("logout success")
            # return render(request, "home.html")
            return Response({"status": "log out success"})

  


class ReportUserOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsReportUser]
    serializer_class=UserSerializer
    authentication_classes = (TokenAuthentication)

    def get_object(self):
        return self.request.user

class CustomerOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsCustomerUser]
    serializer_class=UserSerializer
    authentication_classes = (TokenAuthentication)

    def get_object(self):
        return self.request.user