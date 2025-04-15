import os
from datetime import datetime
from flask import Flask, jsonify, redirect, render_template, request, send_from_directory, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import MetaData

app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)

# WEBSITE_HOSTNAME exists only in production environment
if 'WEBSITE_HOSTNAME' not in os.environ:
    # local development, where we'll use environment variables
    print("Loading config.development and environment variables from .env file.")
    app.config.from_object('azureproject.development')
else:
    # production
    print("Loading config.production.")
    app.config.from_object('azureproject.production')

app.config.update(
    SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialize the database connection
db = SQLAlchemy(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

# The import must be done after db initialization due to circular import issue
from models import Restaurant, Review

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dining_hall/<name>', methods = ['GET'])
def diningHall(name):

    # TODO Write SQL Query to get all food items at dining hall -> {name} 

    sql = f'''
        SELECT DISTINCT *
        FROM public."Dhall" as dh
        LEFT JOIN public."{name}_Calories" as c ON c."Name" = dh."Name"
        WHERE "Location" ILIKE '%{name}%'
    '''

    with db.engine.connect() as conn:
        result = conn.execute(db.text(sql)).fetchall()

    rows = [dict(row._mapping) for row in result]
    return render_template('index.html', results = rows)

@app.route('/meat/<name>', methods = ['GET'])
def meat(name):

    # TODO Write SQL Query to get all food items containing meat -> {name} 

    sql = f'''
    SELECT *
    FROM public."Dhall"
    WHERE "Ingredients" ILIKE '%{name}%' 
    '''

    with db.engine.connect() as conn:
        result = conn.execute(db.text(sql)).fetchall()

    rows = [dict(row._mapping) for row in result]
    return render_template('index.html', results = rows)

@app.route('/meal_type/<name>', methods = ['GET'])
def mealType(name):
    name = name.lower()

    # TODO Write SQL Query to get all food item served during meal_type -> {name} 

    sql = f'''
        SELECT DISTINCT *
        FROM public."Dhall"
        WHERE "Meal Type" ILIKE '%{name}%'
    '''
    
    with db.engine.connect() as conn:
        result = conn.execute(db.text(sql)).fetchall()

    rows = [dict(row._mapping) for row in result]
    return render_template('index.html', results = rows)



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()
