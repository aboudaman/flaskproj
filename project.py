# Minimum flask app
from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
from dbconnect import *

# create instance of this class
app = Flask(__name__)

# List list of restaurants
@app.route('/restaurants/')
def restaurantList():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants= restaurants)


# List menus for restaurants
@app.route('/restaurants/<restaurant_id>/')

def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template("menu.html", restaurant=restaurant, items=items)


# Routes for home page
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

# Create new Menu
@app.route("/restaurants/<restaurant_id>/new/", methods=['GET', 'POST'])
def newMenu(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash ("New Menu Created")
        return render_template('menu_added.html', restaurant_id=restaurant_id)
       
    else:
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

# Edit a Menu
@app.route("/restaurants/<restaurant_id>/<menu_id>/edit/", methods=['GET', 'POST'])
def editMenu(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    print "Edited Items %s" %editedItem
    if request.method == 'POST':
        editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        return render_template('edit_menu.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)


# Delete a menu
@app.route("/restaurants/<restaurant_id>/<menu_id>/delete/", methods=['GET', 'POST'])
def deleteMenu(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('delete.html', restaurant_id=restaurant_id, item=deleteItem)

# Build URL
# with app.test_request_context():
#     print "Inside app test"
    # print url_for('editMenu', restaurant_id='restaurant_id', menu_id='menu_id', )


# Making an API Endpoint (GET Request)
@app.route('/restaurants/<restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(MenuItem=[i.serialize for i in items])

# Making an API Endpoint (GET ALL Restaurants)
@app.route('/restaurants/JSON')
def restaurantListSON():
    restaurant = session.query(Restaurant).all()
    return jsonify(Restaurant=[i.serialize for i in restaurant])

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)