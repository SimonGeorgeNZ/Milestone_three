import os
import pycountry
import re
import unicodedata
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


# --------------Countries-----------------#


@app.route('/get_countries')
def get_countries():
    return render_template('countries.html',
                           countries=mongo.db.countries.find())


@app.route('/new_country')
def new_country():
    return render_template('newcountry.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    countries = []
    input_country = request.form['country_name']
    for country in pycountry.countries:
        countries = country.name
        index = input_country.lower()
        cindex = countries.lower()
        if index in cindex:
            input_country = request.form['country_name']
            find_country = mongo.db.countries.find_one({"country_name": input_country.lower()})
            if find_country:
                return redirect(url_for('get_cities', country_id=find_country['_id']))
            else:
                category_doc = {'country_name': request.form.get('country_name').lower()}
                mongo.db.countries.insert(category_doc)
                country = mongo.db.countries.find_one({'country_name': input_country.lower()})
                return redirect(url_for('new_city', country_id=country['_id']))
    else:
        return redirect(url_for('didyoumean', search = index))


@app.route('/didyoumean/<search>')
def didyoumean(search):
    countries = []
    results = []
    s = search [0]
    for country in pycountry.countries:
        countries = country.name
        cindex = [countries.lower()]
        for place in cindex:
            if place[0] == s:
                results += cindex
        print(results)
    return render_template('didyoumean.html', search = search, results = results)
                

    
    
    




# ---------------Cities-----------------#


@app.route('/new_city/<country_id>')
def new_city(country_id):
    country = mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template('newcity.html', country=country)


@app.route('/get_cities/<country_id>')
def get_cities(country_id):
    country = mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template('cities.html',
    cities = mongo.db.cities.find({"country_name": country['country_name']}),
    country=country)


@app.route('/insert_city', methods=['POST', 'GET'])
def insert_city():
    input_city = request.form['city_name']
    find_city = mongo.db.cities.find_one({"city_name": input_city.lower()})
    if find_city:
        return redirect(url_for('add_review', city_id=find_city['_id']))
    else:
        add_city = {'country_name': request.form.get('country_name').lower(),
        'city_name': request.form.get('city_name').lower()}
        mongo.db.cities.insert_one(add_city)
        new_city = mongo.db.cities.find_one({'city_name': input_city.lower()})
        return redirect(url_for('add_review', city_id=new_city['_id']))


#---------------Reviews-----------------#


@app.route('/add_review/<city_id>')
def add_review(city_id):
    city = mongo.db.cities.find_one({"_id": ObjectId(city_id)})
    return render_template('addtitle.html', city=city)


@app.route('/insert_title', methods=['POST'])
def insert_title():
    add_title = {'city_name': request.form.get('city_name'),
    'review_title': request.form.get('review_title')}
    mongo.db.title.insert(add_title)
    title = mongo.db.title.find_one({'review_title': request.form.get('review_title')})
    return render_template('first_info.html', title=title)


@app.route('/add_review_info', methods=['POST'])
def add_review_info():
    info = mongo.db.first_info
    info.insert_one(request.form.to_dict())
    title = mongo.db.title.find_one({'review_title': request.form.get('review_title')})
    return render_template('accommodation.html', title=title)


@app.route('/insert_accom', methods=['POST'])
def insert_accom():
    accom = mongo.db.accommodation
    accom.insert_one(request.form.to_dict())
    title = mongo.db.accommodation.find_one({'review_title': request.form.get('review_title')})
    return render_template('attractions.html', title=title)


@app.route('/insert_attract', methods=['POST'])
def insert_attract():
    attract = mongo.db.attractions
    attract.insert_one(request.form.to_dict())
    title = mongo.db.attractions.find_one({'review_title': request.form.get('review_title')})
    return render_template('hospitality.html', title=title)


@app.route('/insert_hospo', methods=['POST'])
def insert_hospo():
    hospo = mongo.db.hospitality
    hospo.insert_one(request.form.to_dict())
    title = mongo.db.hospitality.find_one({'review_title': request.form.get('review_title')})
    return render_template('reviewfinal.html', title=title)


@app.route('/insert_final', methods=['POST'])
def insert_final():
    final = mongo.db.reviews
    final.insert_one(request.form.to_dict())
    return render_template('.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

