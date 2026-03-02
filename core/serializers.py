from rest_framework import serializers
from .models import Registro


class RegistroSerializer(serializers.ModelSerializer):
    """
    Serializer encargado de convertir instancias del modelo Registro
    a formato JSON y viceversa.

    También permite validar los datos antes de guardarlos en la base de datos.
    """

    class Meta:
        model = Registro
        fields = "__all__"

    def validate_marca(self, value):
        """
        Validación personalizada para el campo 'marca'.

        Args:
            value (str): Valor recibido desde la petición HTTP.

        Returns:
            str: Valor validado.

        Raises:
            ValidationError: Si el valor no cumple las reglas.
        """
        if len(value) < 3:
            raise serializers.ValidationError(
                "La marca debe tener al menos 3 caracteres."
            )
        return value