import os
import requests
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Meals, Plans, plansToDict


@app.route('/')
def home():
    return render_template('home.html', page_title="Mealer API")


### TODOs ###
# TODO: Make all routes secure by requiring a token to be matched against one in the database for a user


####################
# plans
####################
@app.route('/plans/', defaults={'date': 'all'})
@app.route('/plans/date/<date>')
def plans(date):
    try:
        if (date == 'all'):
            plans = db.session.query(Plans.id, Plans.date,
                                     Meals.title).join(Meals).all()
            # returns a list in this format
            # [(14, datetime.date(2020, 11, 28), 'pbj'),
            #  (15, datetime.date(2020, 11, 28), 'pbj'),
            #  (16, datetime.date(2020, 12, 2), 'pbj')]
            return plansToDict(plans), 200
        else:
            plans = db.session.query(
                Plans.id, Plans.date,
                Meals.title).join(Meals).filter(Plans.date == date).all()
            return plansToDict(plans), 200
    except Exception as err:
        return "Error getting plans from the database. {}".format(err), 400


@app.route('/add-plan/', methods=['POST'])
def add_plan():
    errors = []
    if request.is_json:
        data = request.get_json()
        print(data)
        plan = Plans(date=data.get('date'), meal_id=data.get('meal'))
        db.session.add(plan)
        db.session.commit()
        return str(plan.id), 200


@app.route('/drop-plan/', methods=['POST'])
def drop_plan():
    if request.is_json:
        data = request.get_json()
        Plans.query.filter_by(id=data.get('planId')).delete()
        db.session.commit()
        return "plan deleted", 200


####################
# Meals
####################
@app.route('/meals/')
def all():
    results = ''
    try:
        results = Meals.query.all()
        return jsonify(meals=[meal.serialize for meal in results]), 200
    except:
        return 'Can not return all results', 400


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
            if date:
                datum = datetime.strptime(date,
                                          "%Y-%M-%d").strftime("%Y-%M-%d")
            else:
                datum = ''
            results = {
                'title': title,
                'ingredients': ingredients,
                'instructions': instructions,
                'image': image,
                'url': url,
                'date': datum
            }

            try:
                meal = Meals(title=title,
                             ingredients=ingredients,
                             instructions=instructions,
                             image=image,
                             url=url,
                             date_added=datetime.utcnow())
                db.session.add(meal)
                db.session.flush()

                if date:
                    plan = Plans(date=date, meal_id=meal.id)
                    db.session.add(plan)
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
    except Exception as err:
        errors.append({
            'title': 'Error getting results from database.',
            'message': '{}'.format(err),
            'state': 'error'
        })

    return render_template('show-meals.html',
                           message=errors,
                           results=results,
                           page_title="Mealer | Show Meals")


if __name__ == '__main__':
    app.run()
