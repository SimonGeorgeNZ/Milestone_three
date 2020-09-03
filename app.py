import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Milestone_three'
app.config["MONGO_URI"] = 'mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/Milestone_three?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_countries')
def get_countries():
    return render_template("countries.html", reviews=mongo.db.reviews.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)