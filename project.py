# Minimum flask app
from flask import Flask, render_template
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# create instance of this class
app = Flask(__name__)

@app.route('/restaurants/<restaurant_id>/')

def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ''
    output += "<h1>" 
    output += restaurant.name 
    output += "</h1>"
    output += "<br />"
    output += "<br />"


    for i in items:
        output += i.name
        output += "<br />"
        output += i.price
        output += "<br />"
        output += i.description
        output += "<br />"
    return output

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/home/<name>")
def showName(name):
    info = {
        "me": "hola",
        "name": name,
        "age": 22,

    }

    age = info['age']
    return render_template("index.html", info = info)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)