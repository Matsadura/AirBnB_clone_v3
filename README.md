# AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_amenity(self)` - Test that models/amenity.py conforms to PEP8
* `def test_pep8_conformance_test_amenity(self)` - Test that tests/test_models/test_amenity.py conforms to PEP8
* `def test_amenity_module_docstring(self)` - Test for the amenity.py module docstring
* `def test_amenity_class_docstring(self)` - Test for the Amenity class docstring

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_city(self)` - Test that models/city.py conforms to PEP8
* `def test_pep8_conformance_test_city(self)` - Test that tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Test for the city.py module docstring
* `def test_city_class_docstring(self)` - Test for the City class docstring

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_file_storage(self)` - Test that models/file_storage.py conforms to PEP8
* `def test_pep8_conformance_test_file_storage(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8
* `def test_file_storage_module_docstring(self)` - Test for the file_storage.py module docstring
* `def test_file_storage_class_docstring(self)` - Test for the FileStorage class docstring

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlaceDoc class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_place(self)` - Test that models/place.py conforms to PEP8.
* `def test_pep8_conformance_test_place(self)` - Test that tests/test_models/test_place.py conforms to PEP8.
* `def test_place_module_docstring(self)` - Test for the place.py module docstring
* `def test_place_class_docstring(self)` - Test for the Place class docstring

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReviewDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_review(self)` - Test that models/review.py conforms to PEP8
* `def test_pep8_conformance_test_review(self)` - Test that tests/test_models/test_review.py conforms to PEP8
* `def test_review_module_docstring(self)` - Test for the review.py module docstring
* `def test_review_class_docstring(self)` - Test for the Review class docstring

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestStateDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_state(self)` - Test that models/state.py conforms to PEP8
* `def test_pep8_conformance_test_state(self)` - Test that tests/test_models/test_state.py conforms to PEP8
* `def test_state_module_docstring(self)` - Test for the state.py module docstring
* `def test_state_class_docstring(self)` - Test for the State class docstring

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_user(self)` - Test that models/user.py conforms to PEP8
* `def test_pep8_conformance_test_user(self)` - Test that tests/test_models/test_user.py conforms to PEP8
* `def test_user_module_docstring(self)` - Test for the user.py module docstring
* `def test_user_class_docstring(self)` - Test for the User class docstring

## New Implementations

### 1. Never fail!
We have added extensive unit tests to ensure all functionalities work as expected.

### 2. Improve storage
Two new methods have been added to both `DBStorage` and `FileStorage` classes:
- `get(self, cls, id)`: Retrieves an object based on its class and ID.
- `count(self, cls=None)`: Counts the number of objects in storage. If no class is specified, it returns the count of all objects.

### 3. Status of your API
A new endpoint has been created to return the status of your API:
- **Endpoint**: `/api/v1/status`

### 4. Some stats?
An endpoint has been added to retrieve the number of each object type:
- **Endpoint**: `/api/v1/stats`

### 5. Not found
A handler for 404 errors has been created that returns a JSON-formatted 404 status code response.

### 6. State
Create a new view for State objects that handles all default RESTFul API actions.
- `File`: api/v1/views/states.py
Utilize to_dict() to retrieve an object into valid JSON.
Update api/v1/views/__init__.py to import the new file.
Retrieves the list of all State objects: GET /api/v1/states
`Retrieves a State object`: GET /api/v1/states/<state_id>
`Deletes a State object`: DELETE /api/v1/states/<state_id>
`Creates a State`: POST /api/v1/states
`Updates a State object`: PUT /api/v1/states/<state_id>
### 7. City
Create a new view for City objects that handles all default RESTFul API actions.
`File`: api/v1/views/cities.py
Utilize to_dict() to serialize an object into valid JSON.
Update api/v1/views/__init__.py to import the new file.
Retrieves the list of all City objects of a State: GET /api/v1/states/<state_id>/cities
`Retrieves a City object`: GET /api/v1/cities/<city_id>
`Deletes a City object`: DELETE /api/v1/cities/<city_id>
`Creates a City`: POST /api/v1/states/<state_id>/cities
`Updates a City object`: PUT /api/v1/cities/<city_id>
### 8. Amenity
Create a new view for Amenity objects that handles all default RESTFul API actions.
File: api/v1/views/amenities.py
Utilize to_dict() to serialize an object into valid JSON.
Update api/v1/views/__init__.py to import the new file.
Retrieves the list of all Amenity objects: GET /api/v1/amenities
`Retrieves an Amenity object`: GET /api/v1/amenities/<amenity_id>
`Deletes an Amenity object`: DELETE /api/v1/amenities/<amenity_id>
`Creates an Amenity`: POST /api/v1/amenities
`Updates an Amenity object`: PUT /api/v1/amenities/<amenity_id>
### 9. User
Create a new view for User objects that handles all default RESTFul API actions.
File: api/v1/views/users.py
Utilize to_dict() to retrieve an object into valid JSON.
Update api/v1/views/__init__.py to import the new file.
Retrieves the list of all User objects: GET /api/v1/users
`Retrieves a User object`: GET /api/v1/users/<user_id>
`Deletes a User object`: DELETE /api/v1/users/<user_id>
`Creates a User`: POST /api/v1/users
`Updates a User object`: PUT /api/v1/users/<user_id>
### 10. Place
Create a new view for Place objects that handles all default RESTFul API actions.
File: api/v1/views/places.py
Utilize to_dict() to retrieve an object into valid JSON.
Update api/v1/views/__init__.py to import the new file.
Retrieves the list of all Place objects of a City: GET /api/v1/cities/<city_id>/places
`Retrieves a Place object`: GET /api/v1/places/<place_id>
`Deletes a Place object`: DELETE /api/v1/places/<place_id>
`Creates a Place`: POST /api/v1/cities/<city_id>/places
`Updates a Place object`: PUT /api/v1/places/<place_id>
### 11. Reviews
Create a new view for Review objects that handles all default RESTFul API actions.
File: api/v1/views/places_reviews.py
Utilize to_dict() to retrieve an object into valid JSON.
Update api/v1/views/__init__.py to import the new file.
`Retrieves the list of all Review objects of a Place`: GET /api/v1/places/<place_id>/reviews
`Retrieves a Review object`: GET /api/v1/reviews/<review_id>
`Deletes a Review object`: DELETE /api/v1/reviews/<review_id>
`Creates a Review`: POST /api/v1/places/<place_id>/reviews

### 12. HTTP Access Control (CORS)
Implement CORS (Cross-Origin Resource Sharing) in your Flask API. It's needed to allow web clients from different domains to access your API securely.

### 13. Place - Amenity
Create a new view to manage the connection between Place and Amenity objects. This view will handle adding, removing, and listing amenities associated with places.

### 14. Security Improvements!
Enhance security by encrypting user passwords (MD5 hashing) instead of storing them in plaintext. This ensures better protection against unauthorized access.

### 15. Search
Expand the search functionality of your API. Introduce a new endpoint to search for Place objects based on specified criteria like State, City, and Amenity IDs.


## Bugs
No known bugs at this time. 

## Authors
Zidane Zaoui - [Github](https://github.com/Matsadura)  
Ahadi Cyizere - [Github](http://github.com/PRIEST099)

Second part of Airbnb: Joann Vuong
## License
Public Domain. No copy write protection. 
