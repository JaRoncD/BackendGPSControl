from django.db import models


class Registro(models.Model):
    """
    Modelo que representa un registro dentro del sistema.

    Atributos:
        marca (str): Nombre de la marca asociada.
        sucursal (str): Ubicación o sucursal correspondiente.
        aspirante (str): Nombre del aspirante relacionado.
    """

    marca = models.CharField(
        max_length=100,
        help_text="Nombre de la marca del vehiculo"
    )

    sucursal = models.CharField(
        max_length=100,
        help_text="Nombre de la sucursal"
    )

    aspirante = models.CharField(
        max_length=100,
        help_text="Nombre completo del aspirante"
    )

    def __str__(self):
        """
        Representación legible del objeto en el admin o consola.
        """
        return f"{self.marca} - {self.aspirante}"

    class Meta:
        """
        Configuración adicional del modelo.
        """
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ["id"]