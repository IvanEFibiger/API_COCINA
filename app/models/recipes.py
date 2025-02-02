from . import db
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import desc, asc


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    ingredients = db.Column(ARRAY(db.String), nullable=False)
    portions = db.Column(db.Integer, nullable=False)
    recipe_steps = db.Column(db.String, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False,
                           default=db.func.current_timestamp())

    @classmethod
    def new(cls, title, description, ingredients, portions, recipe_steps, author):
        return Recipe(title=title, description=description, ingredients=ingredients,
                      portions=portions, recipe_steps=recipe_steps, author=author)

    @classmethod
    def get_by_page(cls, order, page, per_page=5):
        sort = desc(Recipe.id) if order == 'desc' else asc(Recipe.id)
        return Recipe.query.order_by(sort).paginate(page=page, per_page=per_page).items

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def __str__(self):
        return self.title