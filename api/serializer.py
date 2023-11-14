from rest_framework import serializers
from .models import chofer, ubicacion


class choferSerializer(serializers.ModelSerializer):
    class Meta:
        model = chofer
        fields = '__all__'
        
        
class ubicacionserializer(serializers.ModelSerializer):
    class Meta:
        model = ubicacion
        fields = '__all__'        
        