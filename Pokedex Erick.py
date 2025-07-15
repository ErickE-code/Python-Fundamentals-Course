import requests as req
import os
import json

API_POKEMON = 'https://pokeapi.co/api/v2/pokemon/{pokemon}'

def call_api(url):
    response = req.get(url)
    if response.status_code == 404:
        return None
    if response.status_code != 200:
        raise Exception(f'API response: {response.status_code}')
    return response.json()

def get_pokemon_data(pokemon_name):
    url = API_POKEMON.format(pokemon=pokemon_name.lower())
    data = call_api(url)
    if not data:
        return None
    
    info = {
        'name': data['name'],
        'id': data['id'],
        'weight': data['weight'],
        'height': data['height'],
        'types': [t['type']['name'] for t in data['types']],
        'abilities': [a['ability']['name'] for a in data['abilities']],
        'moves': [m['move']['name'] for m in data['moves']],
        'image_url': data['sprites']['front_default']
    }
    return info

def save_to_json(pokemon_info):
    os.makedirs('pokedex', exist_ok=True)
    filename = f"pokedex/{pokemon_info['name']}.json"
    with open(filename, 'w') as f:
        json.dump(pokemon_info, f, indent=4)

def show_pokemon(info):
    print(f"Nombre: {info['name']}")
    print(f"ID: {info['id']}")
    print(f"Peso: {info['weight']}")
    print(f"Altura: {info['height']}")
    print(f"Tipos: {', '.join(info['types'])}")
    print(f"Habilidades: {', '.join(info['abilities'])}")
    print(f"Movimientos (primeros 10): {', '.join(info['moves'][:10])}")
    print(f"Imagen: {info['image_url']}")

if __name__ == '__main__':
    nombre = input("Introduce el nombre de un Pokémon: ")
    info = get_pokemon_data(nombre)
    if info:
        show_pokemon(info)
        save_to_json(info)
    else:
        print("Pokémon no encontrado")
