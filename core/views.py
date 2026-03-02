from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Registro
from .serializers import RegistroSerializer
from rest_framework.permissions import IsAuthenticated

class RegistroViewSet(viewsets.ModelViewSet):
    """
    ViewSet que implementa un CRUD completo para el modelo Registro.

    Endpoints generados automáticamente:
        - GET /registros/           -> Lista todos los registros
        - POST /registros/          -> Crea un nuevo registro
        - GET /registros/{id}/      -> Obtiene un registro específico
        - PUT /registros/{id}/      -> Actualiza completamente un registro
        - PATCH /registros/{id}/    -> Actualiza parcialmente un registro
        - DELETE /registros/{id}/   -> Elimina un registro

    Hereda de ModelViewSet para reducir código repetitivo.
    """

    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Sobrescribe el método create para personalizar
        la respuesta al crear un registro.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Registro creado exitosamente",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )