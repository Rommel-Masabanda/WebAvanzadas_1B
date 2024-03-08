from django.urls import resolve
from rest_framework.views import APIView
from .views import ProductoViewSet, AgregarProductoAlCarrito, ObtenerCarrito, EliminarProductoDelCarrito, RealizarCompra

class ApiGatewayMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver_match = resolve(request.path_info)
        view_func = resolver_match.func

        # Verifica si la vista es una instancia de APIView si lo es llama al servicio correspondiente
        if isinstance(view_func, APIView):
            if view_func == ProductoViewSet:
                return ProductoViewSet.as_view()(request)
            elif view_func == AgregarProductoAlCarrito:
                return AgregarProductoAlCarrito.as_view()(request)
            elif view_func == ObtenerCarrito:
                return ObtenerCarrito.as_view()(request)
            elif view_func == EliminarProductoDelCarrito:
                return EliminarProductoDelCarrito.as_view()(request)
            elif view_func == RealizarCompra:
                return RealizarCompra.as_view()(request)
            

        return self.get_response(request)