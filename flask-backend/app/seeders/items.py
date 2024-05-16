from models import Item, db

async def items_by_pokemon_id(pokemon_id):
    return Item.query.filter_by(pokemon_id=pokemon_id).all()

async def add_item(details, pokemon_id):
    item = Item(**details, pokemon_id=pokemon_id)
    db.session.add(item)
    db.session.commit()
    return item

async def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        raise ValueError('Cannot find item')

    db.session.delete(item)
    db.session.commit()
    return item.id

async def update_item(details):
    item_id = details.pop('id')
    item = Item.query.get(item_id)
    if not item:
        raise ValueError('Cannot find item')

    for key, value in details.items():
        setattr(item, key, value)
    db.session.commit()
    return item

