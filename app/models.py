from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()


class PokemonTeam(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    pokemon_id = db.Column(db.Integer, unique=True, nullable=False)
    catch_date = db.Column(db.DateTime)

    

    def __init__(self, name, pokemon_id, catch):
        self.name = name
        self.pokemon_id = pokemon_id
        self.catch = catch
        

    def save(self):
        db.session.add(self)
        db.session.commit()

