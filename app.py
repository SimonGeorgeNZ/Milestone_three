import os
import pycountry
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Milestone_three'
app.config["MONGO_URI"] = 'mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/Milestone_three?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def buttons():
    return render_template('buttons.html')

#--------------Countries-----------------#

@app.route('/get_countries')
def get_countries():
    return render_template('countries.html',
                           countries=mongo.db.countries.find())

@app.route('/add_country')
def add_country():
    return render_template('addcountry.html')

@app.route('/insert_country', methods=['POST'])
def insert_country():
    category_doc = {'country_name': request.form.get('country_name')}
    mongo.db.countries.insert_one(category_doc)
    return redirect(url_for('add_city'))


#---------------Cities-----------------#

@app.route('/get_cities/<country_id>')
def get_cities(country_id):
    country=mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template('cities.html',
    cities = mongo.db.cities.find({"country_name": country['country_name']}))

@app.route('/add_city')
def add_city():
    return render_template('addcity.html',
    new_country=mongo.db.countries.find({natural:1}))

@app.route('/insert_city', methods=['POST'])
def insert_city():
    city = mongo.db.cities
    city.insert_one(request.form.to_dict())
    return redirect(url_for('add_review'))

#---------------Reviews-----------------#

@app.route('/add_review')
def add_review():
    return render_template('addreview.html',
    countries=mongo.db.countries.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
