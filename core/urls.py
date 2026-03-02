from rest_framework.routers import DefaultRouter
from .views import RegistroViewSet

"""
Router de Django REST Framework.

Genera automáticamente las rutas RESTful
para el ViewSet definido.
"""

router = DefaultRouter()
router.register(
    r'registros',
    RegistroViewSet,
    basename='registro'
)

urlpatterns = router.urls