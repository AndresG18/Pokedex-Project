import random

def random_item_images():
    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
    ]
    
    i = random.randint(0, len(images) - 1)
    return images[i]


    print('hello world')