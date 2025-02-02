# API de Recetas

Este proyecto es una API RESTful desarrollada en Flask que permite gestionar recetas, incluyendo su creación, actualización, eliminación y búsqueda.

## Características Principales
- Crear, actualizar, eliminar y buscar recetas.
- Búsqueda de recetas por título, autor o ingredientes.
- Documentación automática con Swagger.

## Tecnologías Utilizadas
- **Backend**: Flask, SQLAlchemy.
- **Base de datos**: PostgreSQL.
- **Documentación**: Flasgger (Swagger).
- **Otras herramientas**: Marshmallow (validación de esquemas).

## Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior.
- PostgreSQL instalado y configurado.

### Pasos para Configurar el Proyecto

1. **Clonar el repositorio**:
   ```
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```
2. **Crear y activar un entorno virtual**:
    ```
   python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
   ```
3. **Instalar dependencias**:
    ```
   pip install -r requirements.txt
   ```
4. **Configurar la Base de datos**:
- Asegúrate de tener PostgreSQL instalado y en ejecución.
- Crea una base de datos en PostgreSQL para el proyecto.
- Configura las variables de entorno en el archivo .env:
   ```
  DATABASE_URL=postgresql://usuario:contraseña@localhost/nombre_de_la_base_de_datos
   ```
5. **Inicializa la Base de datos**:
   ```
    python main.py --setup
   ```
6. **Ejecuta la aplicación**:
   ```
    python main.py
   ```
   
La API estará disponible en http://localhost:5000.

### Uso del proyecto

1. **Obtener todas las recetas**:
   ```
    GET /api/v1/recipes/
   ```
2. **Crear una nueva receta**:
   ```
    POST /api/v1/recipes/
    Body (JSON):
    {
      "title": "Tarta de Manzana",
      "description": "Una deliciosa tarta de manzana.",
      "ingredients": ["manzanas", "harina", "azúcar"],
      "portions": 4,
      "recipe_steps": ["Pelar las manzanas", "Mezclar los ingredientes"],
      "author": "Chef Juan"
    }
   ```
3. **Buscar recetas por ingredientes**:
   ```
    GET /api/v1/recipes/search?ingredients=manzanas,harina
   ```
4. **Buscar recetas por título**:
   ```
    GET /api/v1/recipes/search/title?title=tarta
   ```
   
### Documentación
- La documentación interactiva de la API está disponible en /apidocs/. Aquí puedes probar las rutas y ver los detalles de cada endpoint.

### Notas adicionales:
1. **Variables de entorno**: Asegúrate de que el archivo `.env` esté correctamente configurado con las credenciales de tu base de datos PostgreSQL.
2. **PyCharm**: Si usas PyCharm, no necesitas crear y activar manualmente el entorno virtual, ya que el IDE lo hace automáticamente. Solo asegúrate de que las dependencias estén instaladas (`requirements.txt`).
3. **Documentación**: La documentación interactiva de Swagger estará disponible en `http://localhost:5000/apidocs/` una vez que ejecutes la aplicación.

### Información adicional
Este proyecto fue desarrollado como práctica de desarrollo de APIs con Flask. ¡Siéntete libre de usarlo y modificarlo según tus necesidades!
Mi Linkedin: https://www.linkedin.com/in/ivan-fibiger/
Mi Github: https://github.com/IvanEFibiger