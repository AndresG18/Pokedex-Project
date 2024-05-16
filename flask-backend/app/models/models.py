from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
  __tablename__ = "item"

  id = db.Column(db.Integer, primary_key=True)
  happiness = db.Column(db.Integer)
  imageUrl = db.Column(db.String(255), nullable=False)
  name = db.Column(db.String(255), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  pokemonId = db.Column(db.Integer, nullable=False)
