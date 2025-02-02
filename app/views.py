from flask import Blueprint, request
from .responses import response, not_found, bad_request
from .models.recipes import Recipe
from .schemas import recipe_schema, recipes_schema, params_recipe_schema
from sqlalchemy import or_


api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


def set_recipe(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        recipe = Recipe.query.filter_by(id=id).first()

        if recipe is None:
            return not_found()
        return function(recipe)
    wrap.__name__ = function.__name__
    return wrap

@api_v1.route('/', methods=['GET'])
def index():
    """
    Bienvenido a la API de recetas
    ---
    responses:
      200:
        description: Mensaje de bienvenida
    """
    return {
        'message': 'Bienvenido'
    }


@api_v1.route('/recipes/', methods=['GET'])
def get_recipes():
    """
    Obtener una lista paginada de recetas
    ---
    parameters:
      - name: page
        in: query
        type: integer
        required: false
        default: 1
        description: Número de página
      - name: order
        in: query
        type: string
        required: false
        default: desc
        description: Orden de las recetas (asc o desc)
    responses:
      200:
        description: Lista de recetas
    """
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    recipes = Recipe.get_by_page(order, page)

    return response(recipes_schema.dump(recipes))


@api_v1.route('/recipes/<id>', methods=['GET'])
@set_recipe
def get_recipe(recipe):
    """
    Obtener una receta por su ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la receta
    responses:
      200:
        description: Detalles de la receta
      404:
        description: Receta no encontrada
    """
    return response(recipe_schema.dump(recipe))


@api_v1.route('/recipes', methods=['POST'])
def create_recipe():
    """
    Crear una nueva receta
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            ingredients:
              type: array
              items:
                type: string
            portions:
              type: integer
            recipe_steps:
              type: array
              items:
                type: string
            author:
              type: string
    responses:
      200:
        description: Receta creada exitosamente
      400:
        description: Solicitud inválida
    """
    json = request.get_json(force=True)
    error = params_recipe_schema.validate(json)
    if error:
        return bad_request(error)
    recipe = Recipe.new(json['title'], json['description'], json['ingredients'],
                        json['portions'], json['recipe_steps'], json['author'])
    if recipe.save():
        return response(recipe_schema.dump(recipe))
    return bad_request()


@api_v1.route('/recipes/<id>', methods=['PUT'])
@set_recipe
def update_recipe(recipe):
    """
        Actualizar una receta existente
        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: ID de la receta
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                title:
                  type: string
                description:
                  type: string
                ingredients:
                  type: array
                  items:
                    type: string
                portions:
                  type: integer
                recipe_steps:
                  type: array
                  items:
                    type: string
        responses:
          200:
            description: Receta actualizada exitosamente
          400:
            description: Solicitud inválida
        """
    json = request.get_json(force=True)
    recipe.title = json.get('title', recipe.title)
    recipe.description = json.get('description', recipe.description)
    recipe.ingredients = json.get('ingredients', recipe.ingredients)
    recipe.portions = json.get('portions', recipe.portions)
    recipe.recipe_steps = json.get('recipe_steps', recipe.recipe_steps)

    if recipe.save():
        return response(recipe_schema.dump(recipe))
    return bad_request()


@api_v1.route('/recipes/<id>', methods=['DELETE'])
@set_recipe
def delete_recipe(recipe):
    """
       Eliminar una receta por su ID
       ---
       parameters:
         - name: id
           in: path
           type: integer
           required: true
           description: ID de la receta
       responses:
         200:
           description: Receta eliminada exitosamente
         400:
           description: Solicitud inválida
       """
    if recipe.delete():
        return response(recipe_schema.dump(recipe))
    return bad_request()


@api_v1.route('/recipes/search', methods=['GET'])
def search_recipes_by_ingredients():
    """
    Buscar recetas por ingredientes
    ---
    parameters:
      - name: ingredients
        in: query
        type: string
        required: true
        description: Lista de ingredientes separados por comas
    responses:
      200:
        description: Lista de recetas que coinciden con los ingredientes
      400:
        description: No se proporcionaron ingredientes
    """
    ingredients = request.args.get('ingredients')
    if ingredients:
        ingredient_list = ingredients.split(',')
        conditions = [Recipe.ingredients.contains([ingredient]) for ingredient in ingredient_list]
        recipes = Recipe.query.filter(or_(*conditions)).all()
        print(recipes)
        return response(recipes_schema.dump(recipes))
    return bad_request('No ingredients provided')


@api_v1.route('/recipes/search/title', methods=['GET'])
def search_recipes_by_title():
    """
    Buscar recetas por título
    ---
    parameters:
      - name: title
        in: query
        type: string
        required: true
        description: Título de la receta
    responses:
      200:
        description: Lista de recetas que coinciden con el título
      404:
        description: No se encontraron recetas
      400:
        description: No se proporcionó un título
    """
    title = request.args.get('title')

    if title:
        recipes = Recipe.query.filter(Recipe.title.ilike(f'%{title}%')).all()
        if not recipes:
            return not_found()
        return response(recipes_schema.dump(recipes))

    return bad_request('No title provided')


@api_v1.route('/recipes/search/author', methods=['GET'])
def search_recipes_by_author():
    """
    Buscar recetas por autor
    ---
    parameters:
      - name: author
        in: query
        type: string
        required: true
        description: Nombre del autor
    responses:
      200:
        description: Lista de recetas que coinciden con el autor
      404:
        description: No se encontraron recetas
      400:
        description: No se proporcionó un autor
    """
    author = request.args.get('author')

    if author:
        recipes = Recipe.query.filter(Recipe.author.ilike(f'%{author}%')).all()
        if not recipes:
            return not_found()
        return response(recipes_schema.dump(recipes))

    return bad_request('No author provided')