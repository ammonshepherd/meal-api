from app import db
from sqlalchemy.dialects.postgresql import JSON

 
class Meals(db.Model):
    __tablename__ = 'mealer'
 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    ingredients = db.Column(db.String())
    image = db.Column(db.String())
    url = db.Column(db.String())
 
    def __init__(self, title, description, ingredients, image, url):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.image = image
        self.url = url
 
    def __repr__(self):
        return f"{self.title}:{self.description}:{self.ingredients}:{self.image}:{self.url}"

    @property
    def serialize(self):
        return {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'ingredients': self.ingredients,
                'image': self.image,
                'url': self.url,
                }

