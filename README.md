# SmartRoute Cloud Engine 

Este es el backend oficial del proyecto **SmartRoute**, un motor en la nube diseñado para gestionar, calcular y almacenar rutas geográficas. Está construido con una arquitectura moderna utilizando contenedores y bases de datos gestionadas en la nube.

---

##  Stack Tecnológico

* **Framework:** Django 6.0.3 (Python 3.12)
* **Base de Datos:** PostgreSQL alojado en **Microsoft Azure**
* **Contenedores:** Docker & Docker Desktop
* **Variables de Entorno:** `python-dotenv`
* **CORS (Preparación API):** `django-cors-headers`

---

##  Fases del Proyecto

### Fase A: Infraestructura y Base de Datos (Completada)
1.  **Inicialización de Django:** Creación del proyecto base (`myproject`) y la aplicación principal (`core`).
2.  **Modelado de Datos:** Creación del modelo `Route` con campos geográficos (latitud/longitud para origen y destino) y marcas de tiempo automáticas.
3.  **Dockerización:** Configuración de un entorno reproducible mediante `Dockerfile` (instalando dependencias del sistema como `libpq-dev` y `gcc` para compilar conectores de Postgres).
4.  **Conexión a la Nube:** Transición desde la base de datos local SQLite (`db.sqlite3`) hacia un servidor **PostgreSQL en Azure**, asegurando la conexión mediante variables de entorno (`.env`).
5.  **Persistencia y Administración:** Migraciones ejecutadas con éxito en la nube y creación del superusuario para gestionar los datos a través del panel de administración de Django (`/admin`).

### Fase B: API REST (Próximos pasos)
* Configuración de Django REST Framework.
* Creación de Serializadores para el modelo `Route`.
* Creación de Endpoints (ViewSets/Routers) para servir datos en formato JSON.

---

## Cómo ejecutar el proyecto en local

Para levantar este proyecto en tu máquina, no necesitas instalar Python ni Django directamente, todo funciona a través de **Docker**.

### 1. Variables de Entorno
Debido a medidas de seguridad, las credenciales de la base de datos no se suben al repositorio. Debes crear un archivo `.env` en la raíz del proyecto (al mismo nivel que `manage.py`) con la siguiente estructura:

```env
DB_NAME=postgres
DB_USER=tu_usuario_de_azure
DB_PASSWORD=tu_contraseña
DB_HOST=tu_servidor.postgres.database.azure.com
DB_PORT=5432
```
### 2. Construir la Imagen Docker
Estando en la raíz del proyecto, ejecuta el siguiente comando para construir la imagen con todas las dependencias necesarias:

```
docker build -t smartroute-pro .
```

### 3. Levantar el Contenedor
Una vez construida la imagen, levanta el contenedor interactivo montando tu código local en tiempo real:

```
docker run -it --rm -v ${PWD}:/app -p 8000:8000 smartroute-pro bash
```

### 4. Arrancar el Servidor
Dentro de la terminal del contenedor (root@...:/app#), ejecuta el servidor de desarrollo:

```
python manage.py runserver 0.0.0.0:8000
```

El panel de administración estará disponible en: http://localhost:8000/admin
