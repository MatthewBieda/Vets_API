import enum
import flask  
from flask import request, jsonify

from vetObjects import animal_list

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our program.  In the real world we would want this to be made or come from another source such as a database
PetOwners = [
    {'id': 0,
     'name': 'Keiran',
     'pet_name': 'Seal hunter',
     'pet_type': 'Otter',
     'last_visit_was_for': 'Castration'},
    {'id': 1,
     'name': 'Ahmed',
     'pet_name': 'Mac',
     'pet_type': 'Tortoise',
     'last_visit_was_for': 'Being slow even for a tortoise'},
    {'id': 2,
     'name': 'Gareth',
     'pet_name': 'Captain Jazzy Pants',
     'pet_type': 'Cat',
     'last_visit_was_for': 'Dog bite'},
    {'id': 3,
     'name': 'Matt',
     'pet_name': 'Rex',
     'pet_type': 'Dog',
     'last_visit_was_for': 'Fever'},
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



@app.route('/', methods=['GET']) #tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to our virtual veterinary practice</h1><p>See information on our <a href='/api/animals')>animals</a></p>"


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/customers/', methods=['GET'])
def api_all():
    return jsonify(PetOwners)

@app.route('/api/customers/<int:id>', methods=['GET'])
def get_owner_by_id(id):
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
    return("<h1>Animals / Customers</h1>")

@app.route('/api/animals/', methods=['GET'])
def animals_api_all():
    return jsonify(Animals_JSON)


@app.route('/api/animals/<int:id>', methods=['GET'])
def animals_api_unique(id):
    if id >= len(Animals_JSON):
        return("<h1>ID is invalid</h1>")

    #Take id from url and return corresponding json object
    object = Animals[id]
    available_attributes = vars(object)
    #Vars calls __dict__ method on our object under the hood
    return available_attributes

app.run()
