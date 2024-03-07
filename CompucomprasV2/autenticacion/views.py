from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class RegistroUsuario(APIView):
    def post(self, request):
        # Obtener los datos enviados en la solicitud POST
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Validar que se proporcionen todos los campos requeridos
        if not username or not email or not password:
            return Response({'error': 'Se requiere el nombre de usuario, correo electrónico y contraseña'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Crear un nuevo usuario utilizando la clase User predeterminada de Django
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
        except:
            return Response({'error': 'No se pudo crear el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Devolver una respuesta exitosa
        return Response({'message': 'Usuario registrado exitosamente'}, status=status.HTTP_201_CREATED)