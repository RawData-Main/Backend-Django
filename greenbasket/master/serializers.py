from rest_framework import serializers
from master.models import *
from .serializers import *

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"