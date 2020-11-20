import os
import requests
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Meals, Plans


@app.route('/')
def home():
    return render_template('home.html', page_title="Mealer API")


@app.route('/all/')
def all():
    results = ''
    try:
        results = Meals.query.all()
    except:
        error = 'Can not return all results'
    return jsonify(meals=[meal.serialize for meal in results])


####################
# plans
####################
@app.route('/add-plan/', methods=['POST'])
def add_plan():
    errors = []
    if request.is_json:
        data = request.get_json()
        print(data)
        payload = Plans(date=data.get('date'), meal_id=data.get('meal'))
        db.session.add(payload)
        db.session.commit()
        return "plan added", 200


@app.route('/drop-plan/', methods=['POST'])
def drop_plan():
    if request.is_json:
        data = request.get_json()
        payload = Plans(date=data.get('date'), meal_id=data.get('meal'))
        db.session.delete(payload)
        db.session.commit()
        return "plan deleted", 200


####################
# Meals
####################
@app.route('/meal/<int:id>/')
def meal(id):
    results = ''
    try:
        meal = Meals.query.get(id)
    except:
        error = "No result found"
    return jsonify(meal.serialize)


@app.route('/add-meal/', methods=['GET', 'POST'])
def add_meal():
    message = []
    results = {}

    if request.method == "POST":
        try:
            title = request.form['title']
            ingredients = request.form['ingredients']
            instructions = request.form['instructions']
            image = request.form['image']
            url = request.form['url']
            date = request.form['plan_date']
            results = {
                'title': title,
                'ingredients': ingredients,
                'instructions': instructions,
                'image': image,
                'url': url,
                'date': date
            }

            try:
                meal = Meals(title=title,
                             ingredients=ingredients,
                             instructions=instructions,
                             image=image,
                             url=url,
                             date_added=datetime.utcnow(),
                             date_modified=datetime.utcnow())
                plan = Plans(date=date, meal_id=meal)
                db.session.add(meal)
                db.session.commit()

                message.append({
                    'title': "Successfully added {}".format(title),
                    'state': "success"
                })
            except Exception as err:
                message.append({
                    'title': 'Could not update database.',
                    'message': '{}'.format(err),
                    'state': 'error'
                })
        except Exception as err:
            message.append({
                'title': "Error with form.",
                'message': "{}".format(err),
                'state': 'error'
            })

    return render_template('add-meal.html',
                           page_title="Mealer | Add Meal",
                           message=message,
                           values=results)


@app.route('/show-meals/')
def show_meal():
    errors = []

    try:
        results = Meals.query.all()
    except:
        errors.append('Error getting results from database')

    return render_template('show-meals.html',
                           errors=errors,
                           results=results,
                           page_title="Mealer | Show Meals")


if __name__ == '__main__':
    app.run()
