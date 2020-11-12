# Imports and configurations #

import os
import pycountry
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "Milestone_three"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

MONGO_URI = os.environ.get('MONGO_URI')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')


exceptions = ["England", "Wales", "Scotland", "Northern Ireland", "TEST"]


# Landing page #

@app.route('/')
@app.route('/home')
def home():
    titles = list(mongo.db.title.find().sort("_id", -1).limit(9))
    cities = list(mongo.db.cities.find())
    return render_template('index.html', titles=titles, cities=cities)


# Countries #

    '''Search user input against pycountry names. If
spelling is correct, continue on in the review, if
the spelling is incorrect, redirect to didyoumean.html where
countries starting with the same letter will be displayed'''


@app.route('/new_country')
def new_country():
    return render_template('newcountry.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    countries = []
    input_country = request.form['country_name']
    find_country = mongo.db.countries.find_one(
        {"country_name": input_country.lower()})
    for country in pycountry.countries:
        countries = country.name
        index = input_country.lower()
        cindex = countries.lower()
        if len(index) == 0:
            return render_template('newcountry.html')
        else:
            if len(index) > 1:
                for value in exceptions:
                    if index == cindex or index == value.lower():
                        if find_country:
                            return redirect(url_for('get_cities', country_id=find_country['_id']))
                        else:
                            category_doc = {'country_name': request.form.get(
                                'country_name').lower()}
                            mongo.db.countries.insert(category_doc)
                            country = mongo.db.countries.find_one(
                                {'country_name': input_country.lower()})
                            return redirect(url_for('new_city', country_id=country['_id']))
    else:
        return redirect(url_for('didyoumean', search=index))


@app.route('/didyoumean/<search>')
def didyoumean(search):
    countries = []
    results = []
    s = search[0]
    for country in pycountry.countries:
        countries = country.name
        cindex = [countries.lower()]
        for place in cindex:
            if place[0] == s:
                results += cindex
                for place in results:
                    place = place
    return render_template('didyoumean.html', search=search, results=results, place=place)

    '''Add country that the user clicks on from the list'''


@app.route('/add_list_country/<place>', methods=['POST', 'GET'])
def add_list_country(place):
    find_country = mongo.db.countries.find_one({"country_name": place.lower()})
    if find_country:
        return redirect(url_for('get_cities', country_id=find_country['_id']))
    else:
        new_country = {'country_name': place.lower()}
        mongo.db.countries.insert_one(new_country)
        country = mongo.db.countries.find_one({'country_name': place.lower()})
    return redirect(url_for('new_city', country_id=country['_id']))


# Cities #

    '''Display cities associated with country
to the user for them to select. The user
can add a new city if their city isn't available'''


@app.route('/new_city/<country_id>')
def new_city(country_id):
    country = mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template('newcity.html', country=country)


@app.route('/get_cities/<country_id>')
def get_cities(country_id):
    country = mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template('cities.html',
                           cities=mongo.db.cities.find(
                               {"country_name": country['country_name']}),
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


# Reviews #

    '''The title will act as a password if the user ever
want's to edit or delete their review. The first info dates
will determine if the user will be taken to Accommodation.
If the user selects the same start and end date, it is
determined to be a day trip therefor no accommodation
is needed'''


@app.route('/add_review/<city_id>', methods=['POST', 'GET'])
def add_review(city_id):
    city = mongo.db.cities.find_one({"_id": ObjectId(city_id)})
    return render_template('addtitle.html', city=city)


@app.route('/insert_title', methods=['POST'])
def insert_title():
    input_title = request.form['review_title']
    city = {'city_name': request.form.get('city_name').lower()}
    find_title = mongo.db.title.find_one({"review_title": input_title.lower()})
    if find_title:
       return render_template('addtitle.html', city=city)
    else:
        add_title = {'city_name': request.form.get('city_name').lower(),
                    'review_title': request.form.get('review_title').lower()}
        mongo.db.title.insert_one(add_title)
        title = mongo.db.title.find_one({'review_title': input_title.lower()})
        return render_template('first_info.html', title=title)


@app.route('/add_review_info/<review_id>', methods=['POST', 'GET'])
def add_review_info(review_id):
    info = mongo.db.first_info
    add_info = {'start_date': request.form.get('start_date'),
                'end_date': request.form.get('end_date'),
                'reason': request.form.get('reason'),
                'event': request.form.get('event'),
                's_or_g': request.form.get('s_or_g'),
                'review_title': request.form.get('review_title').lower()}
    start = request.form['start_date']
    end = request.form['end_date']
    title = mongo.db.title.find_one(
        {'review_title': request.form.get('review_title')})
    if start == end:
        info.insert_one(request.form.to_dict())
        return render_template('attractions.html', title=title)
    else:
        info.insert_one(add_info)
        title = mongo.db.title.find_one(
            {'review_title': request.form.get('review_title')})
        return render_template('accommodation.html', title=title)


# Inserting review sections #

    '''Allows the user to either insert the info
to their review, or skip the section if it doesn't
apply to them'''


@app.route('/insert_accom/<review_id>', methods=['POST'])
def insert_accom(review_id):
    title = mongo.db.title.find_one({"_id": ObjectId(review_id)})
    accom = mongo.db.accommodation
    accom.insert_one(request.form.to_dict())
    return render_template('attractions.html', title=title)


@app.route('/insert_another_accom/<review_id>', methods=['POST'])
def insert_another_accom(review_id):
    accom = mongo.db.accommodation
    accom.insert_one(request.form.to_dict())
    title = mongo.db.title.find_one(
        {'review_title': request.form.get('review_title')})
    return render_template('accommodation.html', title=title)


@app.route('/insert_attract/<review_id>', methods=['POST'])
def insert_attract(review_id):
    attract = mongo.db.attractions
    attract.insert_one(request.form.to_dict())
    title = mongo.db.title.find_one(
        {'review_title': request.form.get('review_title')})
    return render_template('hospitality.html', title=title)


@app.route('/insert_another_attract/<review_id>', methods=['POST'])
def insert_another_attract(review_id):
    attract = mongo.db.attractions
    attract.insert_one(request.form.to_dict())
    title = mongo.db.title.find_one(
        {'review_title': request.form.get('review_title')})
    return render_template('attractions.html', title=title)


@app.route('/insert_hospo/<review_id>', methods=['POST'])
def insert_hospo(review_id):
    hospo = mongo.db.hospitality
    hospo.insert_one(request.form.to_dict())
    title = mongo.db.title.find_one(
        {'review_title': request.form.get('review_title')})
    return render_template('reviewfinal.html', title=title)


@app.route('/insert_another_hospo/<review_id>', methods=['POST'])
def insert_another_hospo(review_id):
    hospo = mongo.db.hospitality
    hospo.insert_one(request.form.to_dict())
    title = mongo.db.title.find_one(
        {'review_title': request.form.get('review_title')})
    return render_template('hospitality.html', title=title)


@app.route('/insert_final/<review_id>', methods=['POST', 'GET'])
def insert_final(review_id):
    input_title = request.form['review_title']
    final = mongo.db.reviews
    final.insert_one(request.form.to_dict())
    title = mongo.db.title.find_one({'review_title': input_title.lower()})
    return redirect(url_for('view_review', title=title,
                            review_id=title['_id']))


@app.route('/skip_accom/<review_id>')
def skip_accom(review_id):
    title = mongo.db.title.find_one({"_id": ObjectId(review_id)})
    return render_template('attractions.html', title=title)


@app.route('/skip_attract/<review_id>')
def skip_attract(review_id):
    title = mongo.db.title.find_one({"_id": ObjectId(review_id)})
    return render_template('hospitality.html', title=title)


@app.route('/skip_hospo/<review_id>')
def skip_hospo(review_id):
    title = mongo.db.title.find_one({"_id": ObjectId(review_id)})
    return render_template('reviewfinal.html', title=title)


@app.route('/skip_final/<review_id>')
def skip_final(review_id):
    title = mongo.db.title.find_one({"_id": ObjectId(review_id)})
    return redirect(url_for('view_review', title=title,
                            review_id=title['_id']))


# View reviews #

    '''Displays the users review'''


@app.route('/view_review/<review_id>')
def view_review(review_id):
    title = mongo.db.title.find_one({"_id": ObjectId(review_id)})
    review_title = title['review_title']
    city = title['city_name']
    country = mongo.db.cities.find_one({"city_name": city.lower()})
    first = mongo.db.first_info.find_one(
        {"review_title": review_title.lower()})
    attract = mongo.db.attractions.find(
        {"review_title": review_title.lower()})
    accom = mongo.db.accommodation.find(
        {"review_title": review_title.lower()})
    hospo = mongo.db.hospitality.find({"review_title": review_title.lower()})
    final = mongo.db.reviews.find_one({"review_title": review_title.lower()})
    return render_template('viewreview.html', title=title, first=first,
                           attract=attract, accom=accom, hospo=hospo, final=final, city=city, country=country)


# Edit/update #

    '''Allows the user to edit their review
and save the changes back to MongoDB'''


@app.route('/edit_first/<first_id>')
def edit_first(first_id):
    first = mongo.db.first_info.find_one({"_id": ObjectId(first_id)})
    title = mongo.db.title.find_one({'review_title': first['review_title']})
    return render_template('editfirst.html', title=title, first=first, section_id=first['_id'])


@app.route('/update_first/<first_id>', methods=["POST"])
def update_first(first_id):
    first = mongo.db.first_info
    first.update({'_id': ObjectId(first_id)},
                 {
        'review_title': request.form.get('review_title'),
        'start_date': request.form.get('start_date'),
        'end_date': request.form.get('end_date'),
        'reason': request.form.get('reason'),
        'event': request.form.get('event'),
        's_or_g': request.form.get('s_or_g'),
    })
    input_title = request.form['review_title']
    title = mongo.db.title.find_one({'review_title': input_title.lower()})
    return redirect(url_for('view_review', review_id=title['_id']))


@app.route('/edit_accom/<accom_id>')
def edit_accom(accom_id):
    the_accom = mongo.db.accommodation.find_one({"_id": ObjectId(accom_id)})
    title = mongo.db.title.find_one(
        {'review_title': the_accom['review_title']})
    return render_template('editaccom.html', title=title, accom=the_accom, section_id=the_accom['_id'])


@app.route('/update_accom/<accom_id>', methods=["POST"])
def update_accom(accom_id):
    accom = mongo.db.accommodation
    accom.update({'_id': ObjectId(accom_id)},
                 {
        'review_title': request.form.get('review_title'),
        'accom_name': request.form.get('accom_name'),
        'accom_style': request.form.get('accom_style'),
        'accom_price': request.form.get('accom_price'),
        'accom_site': request.form.get('accom_site'),
        'accom_address': request.form.get('accom_address'),
        'accom_clean': request.form.get('accom_clean'),
        'accom_comment': request.form.get('accom_comment'),
    })
    input_title = request.form['review_title']
    title = mongo.db.title.find_one({'review_title': input_title.lower()})
    return redirect(url_for('view_review', review_id=title['_id']))


@app.route('/edit_attract/<attract_id>')
def edit_attract(attract_id):
    the_attract = mongo.db.attractions.find_one({"_id": ObjectId(attract_id)})
    title = mongo.db.title.find_one(
        {'review_title': the_attract['review_title']})
    return render_template('editattract.html', title=title, attract=the_attract, section_id=the_attract['_id'])


@app.route('/update_attract/<attract_id>', methods=["POST"])
def update_attract(attract_id):
    attract = mongo.db.attractions
    attract.update({'_id': ObjectId(attract_id)},
                   {
        'review_title': request.form.get('review_title'),
        'attract_name': request.form.get('attract_name'),
        'attract_cost': request.form.get('attract_cost'),
        'attract_rating': request.form.get('attract_rating'),
        'attract_site': request.form.get('attract_site'),
        'attract_type': request.form.get('attract_type'),
        'attract_guide': request.form.get('attract_guide'),
        'attract_ticket': request.form.get('attract_ticket'),
        'ticket_site': request.form.get('ticket_site'),
        'attract_time': request.form.get('attract_time'),
        'attract_comment': request.form.get('attract_comment'),
    })
    input_title = request.form['review_title']
    title = mongo.db.title.find_one({'review_title': input_title.lower()})
    return redirect(url_for('view_review', review_id=title['_id']))


@app.route('/edit_hospo/<hospo_id>')
def edit_hospo(hospo_id):
    the_hospo = mongo.db.hospitality.find_one({"_id": ObjectId(hospo_id)})
    title = mongo.db.title.find_one(
        {'review_title': the_hospo['review_title']})
    return render_template('edithospo.html', title=title, hospo=the_hospo, section_id=the_hospo['_id'])


@app.route('/update_hospo/<hospo_id>', methods=["POST"])
def update_hospo(hospo_id):
    hospo = mongo.db.hospitality
    hospo.update({'_id': ObjectId(hospo_id)},
                 {
        'review_title': request.form.get('review_title'),
        'hospo_name': request.form.get('hospo_name'),
        'hospo_style': request.form.get('hospo_style'),
        'hospo_service_rate': request.form.get('hospo_service_rate'),
        'hospo_site': request.form.get('hospo_site'),
        'hospo_hours': request.form.get('hospo_hours'),
        'hospo_cost': request.form.get('hospo_cost'),
        'hospo_overall_rating': request.form.get('hospo_overall_rating'),
        'hospo_comment': request.form.get('hospo_comment'),
    })
    input_title = request.form['review_title']
    title = mongo.db.title.find_one({'review_title': input_title.lower()})
    return redirect(url_for('view_review', review_id=title['_id']))


@app.route('/edit_final/<final_id>')
def edit_final(final_id):
    the_final = mongo.db.reviews.find_one({"_id": ObjectId(final_id)})
    title = mongo.db.title.find_one(
        {'review_title': the_final['review_title']})
    return render_template('editfinal.html', title=title, final=the_final, section_id=the_final['_id'])


@app.route('/update_final/<final_id>', methods=["POST"])
def update_final(final_id):
    final = mongo.db.reviews
    final.update({'_id': ObjectId(final_id)},
                 {
        'review_title': request.form.get('review_title'),
        'reasons_yes': request.form.get('reasons_yes'),
        'reasons_no': request.form.get('reasons_no'),
        'ap_transport': request.form.get('ap_transport'),
        'city_transport': request.form.get('city_transport'),
        'comment_gen': request.form.get('comment_gen'),
    })
    input_title = request.form['review_title']
    title = mongo.db.title.find_one({'review_title': input_title.lower()})
    return redirect(url_for('view_review', review_id=title['_id']))

# Delete #
    '''Allows the user to delete
part or all of their review'''


@app.route('/delete_section/<section_id>/<cat_name>', methods=["GET"])
def delete_section(section_id, cat_name):
    common = mongo.db[cat_name].find_one({"_id": ObjectId(section_id)})
    return render_template('delete.html', cat_name=cat_name, common=common, common_id=common['_id'])


@app.route('/confirm_delete/<review_id>/<cat_name>', methods=['POST', 'GET'])
def confirm_delete(review_id, cat_name):
    common = mongo.db[cat_name].find_one({"_id": ObjectId(review_id)})
    the_title = common['review_title']
    input_title = request.form['is_correct']
    if input_title.lower() == the_title:
        title_main = mongo.db.title.find_one({"review_title": input_title.lower()})
        mongo.db[cat_name].remove({'_id': ObjectId(review_id)})
        return redirect(url_for('view_review', review_id=title_main['_id']))
    else:
        not_quite = "Sorry, that's not the correct title"
        return render_template('delete.html', cat_name=cat_name, common=common, common_id=common['_id'], not_quite=not_quite)


@app.route('/delete_all/<title_id>')
def delete_all(title_id):
    title = mongo.db.title.find_one({"_id": ObjectId(title_id)})
    return render_template('delete.html', common=False, title=title, cat_name=False)


@app.route('/confirm_delete_all/<title_id>', methods=['POST', 'GET'])
def confirm_delete_all(title_id):
    title = mongo.db.title.find_one({"_id": ObjectId(title_id)})
    input_title = request.form['is_correct']
    print(title['review_title'])
    print(input_title)
    if title['review_title'] == input_title.lower():
        mongo.db.first_info.remove({"review_title": input_title}),
        mongo.db.accommodation.remove({"review_title": input_title}),
        mongo.db.attractions.remove({"review_title": input_title}),
        mongo.db.hospitality.remove({"review_title": input_title}),
        mongo.db.reviews.remove({"review_title": input_title}),
        mongo.db.title.remove({"review_title": input_title})
        return redirect(url_for('home'))
    else:
        not_quite = "Sorry, that's not the correct title"
        return render_template('delete.html', common=False, title=title, cat_name=False, not_quite=not_quite)


# Search #

    '''Search for reviews on the landing page'''


@app.route('/review_search', methods=['POST', 'GET'])
def review_search():
    search = request.form['search']
    find_country = mongo.db.countries.find_one({"country_name": search.lower()})
    titles = list(mongo.db.title.find())
    get_cities = list(mongo.db.cities.find({"country_name": search.lower()}))
    if get_cities:
        return render_template('results.html', country=find_country, cities=get_cities, titles=titles)
    elif not get_cities:
        error = "That search doesn't match anything. If you want to it, you can start by adding the country below"
        return render_template('newcountry.html', error=error)


# Search results #

    '''Find the right review after clicking the
link from the search results or the landing page'''


@app.route("/landing_link/<review_id>", methods=['POST', 'GET'])
def landing_link(review_id):
    title = mongo.db.title.find_one({"_id": ObjectId(review_id)})
    review_title = title['review_title']
    city = title['city_name']
    country = mongo.db.cities.find_one({"city_name": city.lower()})
    first = mongo.db.first_info.find_one({"review_title": review_title.lower()})
    attract = mongo.db.attractions.find({"review_title": review_title.lower()})
    accom = mongo.db.accommodation.find({"review_title": review_title.lower()})
    hospo = mongo.db.hospitality.find({"review_title": review_title.lower()})
    final = mongo.db.reviews.find_one({"review_title": review_title.lower()})
    return render_template('landing_link.html', title=title, first=first,
                           attract=attract, accom=accom, hospo=hospo, final=final, city=city, country=country)


# validate #

    '''User validates their review title to
either edit or delete the review'''


@app.route('/validate/<review_id>')
def validate(review_id):
    title = mongo.db.title.find_one({'_id': ObjectId(review_id)})
    the_title = title['review_title']
    return render_template('validate.html', title=title, the_title=the_title)


@app.route('/confirm_title/<review_id>',  methods=['POST', 'GET'])
def confirm_title(review_id):
    title = mongo.db.title.find_one({'_id': ObjectId(review_id)})
    input_title = request.form['is_correct']
    the_title = title['review_title']
    if input_title.lower() == the_title:
        return redirect(url_for('view_review', review_id=title['_id']))
    else:
        not_quite = "Sorry, that's not the correct title"
        return render_template('validate.html', not_quite=not_quite, title=title)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
