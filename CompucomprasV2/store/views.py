from rest_framework import status, viewsets
from .models import Producto
from .serializer import ProductoSerializer
from rest_framework.response import Response



# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    from rest_framework.response import Response

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return Response({'error': 'Esta función no está disponible'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        return Response({'error': 'Esta función no está disponible'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response({'error': 'Esta función no está disponible'}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        return Response({'error': 'Esta función no está disponible'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        return Response({'error': 'Esta función no está disponible'}, status=status.HTTP_400_BAD_REQUEST)




