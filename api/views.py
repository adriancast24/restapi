from rest_framework import viewsets
from .models import chofer,ubicacion
from .serializer import choferSerializer, ubicacionserializer

# Create your views here.


class choferViweSet(viewsets.ModelViewSet):
    queryset = chofer.objects.all()
    serializer_class = choferSerializer

class ubicacionViewSet(viewsets.ModelViewSet):
    queryset = ubicacion.objects.all()
    serializer_class = ubicacionserializer
