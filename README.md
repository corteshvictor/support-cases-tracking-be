# Support Case Tracking Back-end

Este proyecto es un sistema de backend que permite llevar la trazabilidad de casos de soporte que implican acciones manuales en bases de datos transaccionales. Cada caso de soporte está relacionado con una solicitud que puede requerir modificaciones manuales en una base de datos externa. El sistema registra cada cambio realizado, almacenando información como la tabla afectada, la columna, los valores anteriores y nuevos, y quién realizó la modificación.

## Requerimiento

El objetivo de este proyecto es auditar y hacer un seguimiento detallado de los casos de soporte que requieren cambios manuales en bases de datos transaccionales. Las funcionalidades principales incluyen:

1. **Registro de casos de soporte**: Detallar la información sobre un caso de soporte, como la base de datos y la consulta SQL ejecutada.
2. **Registro de cambios manuales**: Auditar las modificaciones manuales en cualquier base de datos, capturando detalles como la tabla, columna, valores anteriores y nuevos, y el usuario que realizó el cambio.
3. **API de FastAPI**: Proveer una API para la creación y consulta de casos de soporte y los registros de auditoría.

Este sistema utiliza **FastAPI** como framework web y **PostgreSQL** como base de datos, siguiendo una arquitectura limpia (hexagonal).

## Requerimientos técnicos

- Python 3.x
- PostgreSQL
- FastAPI

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/corteshvictor/support-case-tracking-be.git
```

2. Crear un entorno virtual para gestionar las dependencias:

```bash
python -m venv .venv
source .venv/env/bin/activate
```

**Nota:** Mayor información https://fastapi.tiangolo.com/virtual-environments/

3. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuración de variables de entorno

Para configurar las variables de entorno, copia el contenido del archivo `.env.example` y crea un archivo `.env` dentro de la carpeta `src`. Completa las variables de entorno necesarias para la conexión a tu base de datos PostgreSQL:

```bash
DB_NAME=support_case_management
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Creación de la base de datos y tablas

Una vez instaladas las dependencias y configurado el archivo `.env`, puedes ejecutar los scripts para inicializar la base de datos y poblarla con datos de ejemplo:

```bash
python scripts/init_db.py
```

## Ejecutar el servidor

Para iniciar el servidor FastAPI en modo desarrollo, ejecuta el siguiente comando:

```bash
fastapi dev src/main.py
```

Esto levantará la API en el puerto predeterminado (generalmente http://127.0.0.1:8000), donde podrás interactuar con los endpoints disponibles para manejar los casos de soporte y la auditoría de los cambios manuales en la base de datos.

## Documentación de la API

FastAPI genera dos tipos de documentación interactiva para el API:

1. **Swagger UI:** Una interfaz de usuario interactiva que permite explorar y probar los endpoints de la API. Puedes acceder a Swagger UI en:

```
http://127.0.0.1:8000/docs
```

2. **ReDoc:** Una documentación estática que proporciona una vista estructurada y detallada de la API. Puedes acceder a ReDoc en:

```
http://127.0.0.1:8000/redoc
```
