# 🗺️ BackendGPSControl

Backend REST API para un sistema de control y monitoreo GPS, construido con **Django** y **Django REST Framework**. Provee autenticación mediante JWT y está listo para despliegue en plataformas como Heroku o Railway.

---

## 🚀 Tecnologías

| Tecnología | Versión |
|---|---|
| Python | 3.x |
| Django | 4.2.28 |
| Django REST Framework | 3.16.1 |
| SimpleJWT | 5.5.1 |
| Gunicorn | 23.0.0 |
| PostgreSQL (psycopg2-binary) | 2.9.11 |
| django-cors-headers | 4.9.0 |
| WhiteNoise | 6.11.0 |

---

## 📁 Estructura del proyecto

```
BackendGPSControl/
├── core/               # Configuración principal del proyecto Django
├── crud/               # Aplicación principal con modelos, vistas y URLs
│   └── wsgi.py         # Punto de entrada WSGI
├── manage.py           # CLI de Django
├── Procfile            # Configuración de despliegue (Gunicorn)
├── requirements.txt    # Dependencias del proyecto
└── db.sqlite3          # Base de datos local (desarrollo)
```

---

## ⚙️ Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/JaRoncD/BackendGPSControl.git
cd BackendGPSControl
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
SECRET_KEY=tu_secret_key_aqui
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3   # o tu URL de PostgreSQL
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`.

---

## 🔐 Autenticación

Este proyecto usa **JWT (JSON Web Tokens)** mediante `djangorestframework-simplejwt`.

### Obtener tokens

```http
POST /api/token/
Content-Type: application/json

{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```

**Respuesta:**
```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

### Refrescar el access token

```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "<refresh_token>"
}
```

### Usar el token en peticiones protegidas

```http
Authorization: Bearer <access_token>
```

---

## 🌐 Endpoints principales

> Los endpoints pueden variar según la configuración en `crud/urls.py`.

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/api/token/` | Obtener access y refresh token |
| POST | `/api/token/refresh/` | Refrescar el access token |
| GET | `/api/...` | Listado de recursos GPS |
| POST | `/api/...` | Crear nuevo recurso |
| PUT/PATCH | `/api/.../id/` | Actualizar recurso |
| DELETE | `/api/.../id/` | Eliminar recurso |

---

## ☁️ Despliegue

El proyecto incluye un `Procfile` configurado para Gunicorn, compatible con plataformas como **Heroku** o **Railway**.

```
web: gunicorn crud.wsgi
```

### Variables de entorno recomendadas para producción

```env
SECRET_KEY=clave_segura_en_produccion
DEBUG=False
DATABASE_URL=postgres://usuario:contraseña@host:5432/nombre_db
ALLOWED_HOSTS=tu-dominio.com
```

### Pasos en Heroku

```bash
heroku create nombre-de-tu-app
heroku config:set SECRET_KEY=... DEBUG=False DATABASE_URL=...
git push heroku main
heroku run python manage.py migrate
```

---

## 🛡️ CORS

El proyecto tiene `django-cors-headers` instalado. Configura los orígenes permitidos en `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://tu-frontend.com",
]
```

---

## 🗄️ Base de datos

- **Desarrollo:** SQLite (`db.sqlite3`)
- **Producción:** PostgreSQL (configurado vía `DATABASE_URL` con `dj-database-url`)

---

## 📄 Licencia

Este proyecto es de uso privado/académico. Contacta al autor para más información.

---

## 👤 Autor

**JaRoncD** — [github.com/JaRoncD](https://github.com/JaRoncD)
