import os
import requests
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Meals, Plans


@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/add-plan/', methods=['POST'])
def add_plan():
    errors = []
    if request.is_json:
        data = request.get_json()
        print(data)
        payload = Plans(
                date = data.get('date'),
                meal_id = data.get('meal')
                )
        db.session.add(payload)
        db.session.commit()
        return "plan added", 200

@app.route('/drop-plan/', methods=['POST'])
def drop_plan():
    if request.is_json:
        data = request.get_json()
        payload = Plans(
                date = data.get('date'),
                meal_id = data.get('meal')
                )
        db.session.delete(payload)
        db.session.commit()
        return "plan deleted", 200



@app.route('/add-meal/', methods=['GET', 'POST'])
def add_meal():
    errors = []
    results = {}

    if request.method == "POST":
        try:
            title = request.form['title']
            instructions = request.form['instructions']
            ingredients = request.form['ingredients']
            image = request.form['image']
            url = request.form['url']
        except:
            errors.append("Unable to submit form.")

        try:
            result = Meals(
                    title = title,
                    instructions = instructions,
                    ingredients = ingredients,
                    image = image,
                    url = url
                    )
            db.session.add(result)
            db.session.commit()
        except:
            errors.append('Could not update database')

    return render_template('add-meal.html', errors=errors)


@app.route('/show-meals/')
def show_meal():
    errors = []
    
    try:
        results = Meals.query.all()
    except:
        errors.append('Error getting results from database')

    return render_template('show-meals.html', errors=errors, results=results)

@app.route('/all/')
def all():
    results = ''
    try:
        results = Meals.query.all()
    except:
        error = 'Can not return all results'
    return jsonify(meals = [meal.serialize for meal in results])

@app.route('/meal/<int:id>/')
def meal(id):
    results = ''
    try: 
        meal = Meals.query.get(id)
    except:
        error = "No result found"
    return jsonify(meal.serialize)


if __name__ == '__main__':
    app.run()

