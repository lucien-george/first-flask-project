from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

restaurants = [
  {
    "id": 1,
    "name": "Dishoom",
    "address": "London"
  }
]

@app.route('/restaurants')
def index():
  # return render_template('index.html', restaurants=restaurants)
  return jsonify(restaurants)

@app.route('/restaurants/<id>')
def show(id):
  for restaurant in restaurants:
    if restaurant['id'] == int(id):
      return jsonify(restaurant)
  return jsonify({ "error": "Not found" })

@app.route('/restaurants/new')
def new():
  pass

@app.route('/restaurants', methods=['POST'])
def create():
  data = request.get_json()
  new_restaurant = {
    "id": restaurants[-1]['id'] + 1,
    "name": data['name'],
    "address": data['address']
  }
  restaurants.append(new_restaurant)
  return jsonify(new_restaurant)

@app.route('/restaurants/<id>/edit')
def edit(id):
  for restaurant in restaurants:
    if restaurant['id'] == int(id):
      return jsonify(restaurant)
  return jsonify({ "error": "Not found" })

@app.route('/restaurants/<id>', methods=['PATCH'])
def update(id):
  data = request.get_json()
  for restaurant in restaurants:
    if restaurant['id'] == int(id):
      restaurant['name'] = data['name']
      restaurant['address'] = data['address']
      return jsonify(restaurant)
  return jsonify({ "error": "Not found" })

@app.route('/restaurants/<id>', methods=['DELETE'])
def destroy(id):
  for restaurant in restaurants:
    if restaurant['id'] == int(id):
      restaurants.remove(restaurant)
      return jsonify({})
  return jsonify({ "error": "not found"})

app.run(port=3000)
