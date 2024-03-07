from rest_framework import status, viewsets
from .models import Producto, CarritoProducto, Carrito, Banner
from .serializer import ProductoSerializer, CarritoProductoSerializer, CarritoSerializer, BannerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

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



class AgregarProductoAlCarrito(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        producto_id = request.data.get('producto_id')
        cantidad = int(request.data.get('cantidad', 1))  
        
        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
        item_carrito, creado_item = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
        
        if not creado_item:
            item_carrito.cantidad += cantidad
        else:
            item_carrito.cantidad = cantidad
        
        item_carrito.save()
        
        carrito.total += producto.precio * cantidad
        carrito.cantidad_productos += cantidad
        carrito.save()
        
        return Response({'message': 'Producto agregado al carrito'}, status=status.HTTP_201_CREATED)
    

class ObtenerCarrito(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        carritos = Carrito.objects.filter(usuario=request.user).prefetch_related('productos')
        banners = Banner.objects.all()
        carritos_serializer = CarritoSerializer(carritos, many=True)
        banners_serializer = BannerSerializer(banners, many=True)
        data = {
            'carritos': carritos_serializer.data,
            'banners': banners_serializer.data
        }
        return Response(data)
    

class EliminarProductoDelCarrito(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        item_carrito_id = request.data.get('item_carrito_id')
        
        item_carrito = get_object_or_404(CarritoProducto, id=item_carrito_id)
        
        cantidad_producto = item_carrito.cantidad
        precio_producto = item_carrito.producto.precio

        carrito = item_carrito.carrito
        
        carrito.total -= precio_producto
        
        if cantidad_producto > 1:
            item_carrito.cantidad -= 1
            carrito.cantidad_productos -= 1  
            item_carrito.save()
        else:
            item_carrito.delete()
            carrito.cantidad_productos -= 1  
        
        carrito.save()
        
        return Response({'message': 'Producto eliminado del carrito'}, status=status.HTTP_200_OK)

class RealizarCompra(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        item_carrito_id = request.data.get('item_carrito_id')
        carrito = get_object_or_404(Carrito, id=item_carrito_id)
        
        carrito.productos.clear()
        carrito.total = 0
        carrito.cantidad_productos = 0
        carrito.save()
        
        return Response({'message': 'Compra realizada'}, status=status.HTTP_200_OK)
