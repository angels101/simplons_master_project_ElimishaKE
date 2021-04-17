from rest_framework import serializers
from . models import ElimishaMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElimishaMerch
        fields = ('id', 'name', 'description' 'price')