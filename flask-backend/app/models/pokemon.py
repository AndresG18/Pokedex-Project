from .db import db
import json

UNKNOWN_IMG_URL = "/images/unknown.png"

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]

class Pokemon(db.Model):
  __tablename__ = "pokemon"

  id = db.Column(db.Integer, primary_key=True)
  number = db.Column(db.Integer, unique=True, nullable=False)
  attack = db.Column(db.Integer, nullable=False)
  defense = db.Column(db.Integer, nullable=False)
  imageUrl = db.Column(db.String, nullable=False)
  name = db.Column(db.String(255), nullable=False, unique=True)
  type = db.Column(db.Enum(*types), nullable=False)
  moves = db.Column(db.String(255), nullable=False)
  encounter_rate = db.Column(db.Numeric(3,2))
  catch_rate = db.Column(db.Numeric(3, 2))
  captured = db.Column(db.Boolean, default=False)

  items = db.relationship('Item', back_populates='pokemon')

  @property
  def image_url(self):
    return self.image_url if self.captured else UNKNOWN_IMG_URL

  @property
  def moves_list(self):
    return json.loads(self.moves) if self.moves else []

  @moves_list.setter
  def moves_list(self, val):
    self.moves = json.dumps(val)

  def to_dict(self):
    return {
      'id': self.id,
      'number': self.number,
      'attack': self.attack,
      'defense': self.defense,
      'imageUrl': self.imageUrl,
      'name': self.name,
      'type': self.type,
      'moves': self.movesList,
      'encounterRate': self.encounter_rate,
      'catchRate': self.catch_rate,
      'captured': self.captured,
      'items': [item.to_dict() for item in self.items]
    }
