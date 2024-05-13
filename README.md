# Movies-API REST

Here is a basic but practical REST API. It helps us practice consuming an API. This API is developed using FastAPI, creating a basic CRUD with the SQLAlchemy ORM and JWT authentication.

### Features
* Add new movie
* Edit movie
* Delete single movie
* Get movies by Id and category

### Technologies used:
* python
* FastAPI
* SQLAlchemy
* PyJWT
* SQLite
* Git
* Patron N capas

## Development environment

* `python -m venv <Environment name>` : Create the virtual Environment.

* Linux : `source env/bin/activate` | Windows : `env\Scripts\activate` : We activate the virtual environment.

* `pip install -r requirements.txt` : We recreate the virtual environment.

* `uvicorn main:app --reload` : to run the api.

Open [http://localhost:8000/docs](http://localhost:8000/docs) to view the api in your browser.
