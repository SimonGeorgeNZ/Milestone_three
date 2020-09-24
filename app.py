import os
import pycountry
from flask import Flask, render_template, redirect, request, url_for, flash
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

@app.route('/new_country')
def new_country():
    return render_template('newcountry.html')

@app.route('/insert_country', methods=['POST', 'GET'])
def insert_country():
    input_country = request.form['country_name']
    print(input_country)
    find_country = mongo.db.countries.find_one({"country_name":input_country.lower()})
    print(find_country)
    if find_country:
        return redirect(url_for('get_cities', country_id=find_country['_id']))
    else:
        category_doc = {'country_name': request.form.get('country_name').lower()}
        mongo.db.countries.insert(category_doc)
        country=mongo.db.countries.find_one({'country_name': input_country.lower()})
        return redirect(url_for('new_city', country_id=country['_id']))
    

#---------------Cities-----------------#

@app.route('/new_city/<country_id>')
def new_city(country_id):
    country=mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template('newcity.html', country = country)

@app.route('/get_cities/<country_id>')
def get_cities(country_id):
    country=mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template('cities.html',
    cities = mongo.db.cities.find({"country_name": country['country_name']}),
    country = country)


@app.route('/insert_city', methods=['POST'])
def insert_city():
    mongo.db.cities.insert_one(request.form.to_dict())
    new_city=mongo.db.cities.find_one({'city_name': request.form.get('city_name')})
    return redirect(url_for('add_review', city_id = new_city['_id']))


#---------------Reviews-----------------#

@app.route('/add_review/<city_id>')
def add_review(city_id):
    city=mongo.db.cities.find_one({"_id": ObjectId(city_id)})
    return render_template('addtitle.html', city=city)

@app.route('/insert_title', methods=['POST'])
def insert_title():
    title = mongo.db.title
    title.insert_one(request.form.to_dict())
    return redirect(url_for('add_review'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
