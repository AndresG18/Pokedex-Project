from flask import Blueprint

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


@bp.route('/')
def all_pokemon():
    pokemon = PokemonRepository.list()
    return jsonify(pokemon)

@bp.route('/', methods=['POST'])                    # incomplete
def create_pokemon():
    id = PokemonRepository.create(request.json)
    return redirect()



@bp.route('/types')
def get_types():
    return jsonify(types)


@bp.route('/random')
def get_random():
    random_pokemon = PokemonRepository.random()
    return jsonify(random_pokemon)

@bp.route('/battle')
def battle():
    ally_id = request.args.get('allyId')
    op_id = request.args.get('opponentId')
    pokemon = PokemonRepository.battle(ally_id, op_id)
    return jsonify(pokemon)

@bp.route('/<int:id>')
def pokemon_by_id(id):
    pokemon = PokemonRepository.one(id)
    return jsonify(pokemon)

@bp.route('/<int:id>/items')
def get_item(id):
    items = ItemsRepository.items_by_pokemon_id(id)
    return jsonify(items)

@bp.route('/<int:id>/items', methods=['POST'])              # ????
def add_item(id):
    pass