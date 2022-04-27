import enum
import flask  
from flask import request, jsonify

from vetObjects import animal_list

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our program.  In the real world we would want this to be made or come from another source such as a database
PetOwners = [
    {'id': 0,
     'name': 'Keiran'},
    {'id': 1,
     'name': 'Ahmed'},
    {'id': 2,
     'name': 'Gareth'},
    {'id': 3,
     'name': 'Matt'}
]

Animals = animal_list
Animals_JSON = []
for id, animal in enumerate(Animals):
    Animals_JSON_iter = {
        'id': id,
        'animal': str(animal)
    }
    Animals_JSON.append(Animals_JSON_iter)

print(Animals_JSON)

#Mapping owners to pets
for i in range(len(Animals)):
    PetOwners[i]["owner of"] = str(Animals[i])

print(PetOwners)


@app.route('/', methods=['GET']) #tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return (
    "<h1>Welcome to our virtual veterinary practice API</h1><p>See information on our <a href='/api/animals')>animals</a> and <a href='/api/customers')>customers</a>.</p>"
    "<p>We provide a standard REST API.</p>"
    "<p>Animals can also be <a href='/api/animals/agequery?age=10')>queried via age.</a></p>"
    "<a href='/api/customers/3'>Customer example</a> <br>"
    "<a href='/api/animals/3'>Animal example</a>"
    )

# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/customers/', methods=['GET'])
def api_all():
    return jsonify(PetOwners)

@app.route('/api/customers/<int:id>', methods=['GET'])
def get_owner_by_id(id):
    if id >= len(PetOwners):
        return("<h1>ID is invalid</h1>")

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for PetOwner in PetOwners:
        if PetOwner['id'] == id:
            results.append(PetOwner)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


@app.route('/api/')
def redirect():
    return("<h1><a href='/api/animals')>Animals</a> <br><br> <a href='/api/customers')>Customers</a></h1>")

#List view for all animals
@app.route('/api/animals/', methods=['GET'])
def animals_api_all():
    return jsonify(Animals_JSON)

#Detail view for animals
@app.route('/api/animals/<int:id>', methods=['GET'])
def animals_api_unique(id):
    if id >= len(Animals_JSON):
        return("<h1>ID is invalid</h1>")

    #Take id from url and return corresponding json object
    object = Animals[id]
    available_attributes = vars(object)
    #Vars calls __dict__ method on our object under the hood
    return available_attributes


#Adding a route that enables searching for animals by their age
@app.route('/api/animals/agequery', methods=['GET'])
def animals_by_age():
    # Check if an age was provided as part of the URL.
    # If age is provided, assign it to a variable.
    # If no age is provided, display an error in the browser.
    if 'age' in request.args:
        age = int(request.args['age'])
    else:
        return "Error: Invalid query."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested age.
    for animal in Animals:
        if 'age' in vars(animal):
            if animal.age == age:
                results.append(str(animal))
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    if len(results) == 0:
        return("<h1>No animals found which match that query</h1>")
    return jsonify(results)


app.run()
