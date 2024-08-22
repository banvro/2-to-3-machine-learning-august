from rest_framework import serializers
from myapis.models import Contactus

class contactusserlizer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        # fields = '__all__'
        fields = ["username", "email"]
