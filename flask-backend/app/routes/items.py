from flask import Blueprint

bp = Blueprint("items", __name__, url_prefix="/api/items")

@bp.route("/:id")
def hello ():
  return "Hello Wor;d"
