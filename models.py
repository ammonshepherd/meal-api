from app import db
from datetime import datetime


class Meals(db.Model):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    instructions = db.Column(db.Text())
    ingredients = db.Column(db.Text())
    image = db.Column(db.Text())
    url = db.Column(db.Text())
    date_added = db.Column(db.DateTime(),
                           nullable=False,
                           default=datetime.utcnow())
    date_modified = db.Column(db.DateTime(),
                              nullable=False,
                              default=datetime.utcnow(),
                              onupdate=datetime.utcnow())
    plans = db.relationship('Plans', backref='meals', lazy=True)

    def __repr__(self):
        return f"{self.title}:{self.instructions}:{self.ingredients}:{self.image}:{self.url}:{self.date_added}:{self.date_modified}"

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'instructions': self.instructions,
            'ingredients': self.ingredients,
            'image': self.image,
            'url': self.url,
            'date_added': self.date_added,
            'date_modified': self.date_modified,
        }


class Plans(db.Model):
    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey("meals.id"), nullable=False)

    def __repr__(self):
        return f"{self.date}:{self.meal_id}"

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'meal': self.meal_id,
        }
