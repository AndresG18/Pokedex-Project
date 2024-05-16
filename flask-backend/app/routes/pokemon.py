from flask import Blueprint
# from ..models import db,

bp = Blueprint("pokemon", __name__, url_prefix="/api/pokemon")

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
];

@bp.route("/types")
def getTypes():
  return { "types": types }
