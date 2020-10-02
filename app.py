# app.py
import os
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Meals


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/add-meal/', methods=['GET', 'POST'])
def add_meal():
    errors = []
    results = {}

    if request.method == "POST":
        try:
            title = request.form['title']
            description = request.form['description']
            ingredients = request.form['ingredients']
            image = request.form['image']
            url = request.form['url']
        except:
            errors.append("Unable to submit form.")

        try:
            result = Meals(
                    title = title,
                    description = description,
                    ingredients = ingredients,
                    image = image,
                    url = url
                    )
            db.session.add(result)
            db.session.commit()
        except:
            errors.append('Could not update database')

    return render_template('add-meal.html', errors=errors)


if __name__ == '__main__':
    app.run()

