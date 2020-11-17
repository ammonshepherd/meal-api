from app import db
from sqlalchemy.dialects.postgresql import JSON

 
class Meals(db.Model):
    __tablename__ = 'meals'
 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    instructions = db.Column(db.String())
    ingredients = db.Column(db.String())
    image = db.Column(db.String())
    url = db.Column(db.String())
 
    def __init__(self, title, instructions, ingredients, image, url):
        self.title = title
        self.instructions = instructions
        self.ingredients = ingredients
        self.image = image
        self.url = url
 
    def __repr__(self):
        return f"{self.title}:{self.instructions}:{self.ingredients}:{self.image}:{self.url}"

    @property
    def serialize(self):
        return {
                'id': self.id,
                'title': self.title,
                'instructions': self.instructions,
                'ingredients': self.ingredients,
                'image': self.image,
                'url': self.url,
                }

class Plans(db.Model):
    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    meal_id = db.Column(db.Integer)


    def __init__(self, date, meal_id):
        self.date = date
        self.meal_id = meal_id

    def __repr__(self):
        return f"{self.date}:{self.meal_id}"

    @property
    def serialize(self):
        return {
                'id': self.id,
                'date': self.date,
                'meal': self.meal_id,
                }
