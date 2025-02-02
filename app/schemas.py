from marshmallow import Schema, fields
from marshmallow.validate import Length


class RecipeSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'ingredients', 'portions', 'recipe_steps', 'author')



class ParamsRecipeSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=50))
    description = fields.Str(required=True, validate=Length(max=250))
    ingredients = fields.List(fields.Str(), required=True, validate=Length(min=1))
    portions = fields.Int(required=True)
    recipe_steps = fields.Str(required=True)
    author = fields.Str(required=True, validate=Length(max=50))


recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)
params_recipe_schema = ParamsRecipeSchema()