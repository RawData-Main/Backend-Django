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
    
# class LogoutView(View):
#     def get(self, request):
#         logout(request)


#-------------------------------------------------------------#

# def LogoutView(request,format=None):
#     logout(request)

#----------------------------------------------------#

class LogoutView(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)



class ReportUserOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsReportUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class CustomerOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsCustomerUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user