import random
from faker import Faker
from models import Pokemon, db

fake = Faker()

def random_100():
    return random.randint(1, 100)

def random_image():
    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
    ]
    return random.choice(images)

def generate_items():
    for _ in range(3):
        yield {
            'name': fake.word(),
            'price': random_100(),
            'happiness': random_100(),
            'imageUrl': random_image()
        }

async def create(details):
    items = list(generate_items())
    pokemon = Pokemon(**details)
    for item_details in items:
        pokemon.items.append(Item(**item_details))
    db.session.add(pokemon)
    db.session.commit()
    return pokemon.id

async def update(details):
    id = details.pop('id')
    pokemon = Pokemon.query.filter_by(id=id).first()
    if pokemon:
        for key, value in details.items():
            setattr(pokemon, key, value)
        db.session.commit()
        return id
    else:
        return None

async def list_pokemon():
    return Pokemon.query.all()

async def get_one(id):
    return Pokemon.query.filter_by(id=id).first()

async def random_pokemon():
    pokemon = Pokemon.query.all()
    encounter_rate_sum = sum(p.encounter_rate for p in pokemon)
    random_sum = random.random() * encounter_rate_sum
    chosen_pokemon = None
    for p in pokemon:
        if random_sum < p.encounter_rate:
            chosen_pokemon = p
            break
        random_sum -= p.encounter_rate
    return chosen_pokemon

async def battle(ally_id, opponent_id):
    ally = Pokemon.query.get(ally_id)
    opponent = Pokemon.query.get(opponent_id)
    if not ally:
        raise ValueError('Ally Pokemon not found')
    if not opponent:
        raise ValueError('Opponent Pokemon not found')

    min_capture_rate = 30
    attack_diff = ally.attack - opponent.defense
    if attack_diff < min_capture_rate:
        attack_diff = min_capture_rate

    random_num = random.random() * 100

    if random_num <= attack_diff:
        opponent.captured = True
        db.session.commit()
        return opponent
    else:
        return opponent


