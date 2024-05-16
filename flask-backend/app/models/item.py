from .db import db

class Item(db.Model):
  __tablename__ = "item"

  id = db.Column(db.Integer, primary_key=True)
  happiness = db.Column(db.Integer)
  imageUrl = db.Column(db.String(255), nullable=False)
  name = db.Column(db.String(255), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  pokemon_id = db.Column(db.Integer, nullable=False)

  pokemon = db.relationship('Pokemon', back_populates='items')

  def to_dict(self):
    return {
      'id': self.id,
      'happiness': self.happiness,
      'imageUrl': self.image_url,
      'name': self.name,
      'price': self.price,
      'pokemonId': self.pokemon_id
    }
