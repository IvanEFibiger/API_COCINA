from flask import Flask
from flasgger import Swagger  # Importa Swagger
from .models import db
from .models.recipes import Recipe
from .views import api_v1

app = Flask(__name__)

def create_app(environment):
    # Cargar la configuración desde el entorno
    app.config.from_object(environment)

    # Configuración de Swagger
    app.config['SWAGGER'] = {
        'title': 'API de Recetas',
        'version': '1.0',
        'description': 'Documentación de la API de Recetas',
        'uiversion': 3  # Usar Swagger UI 3
    }
    Swagger(app)  # Inicializa Swagger en la aplicación Flask

    # Registrar el Blueprint
    app.register_blueprint(api_v1)

    # Inicializar la base de datos
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

