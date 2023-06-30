import requests
import json
import os

def obtener_informacion_pokemon(nombre_pokemon):
    url_base = "https://pokeapi.co/api/v2/pokemon/"
    url = url_base + nombre_pokemon.lower()

    respuesta = requests.get(url)

    if respuesta.status_code == 404:
        return None

    datos_pokemon = respuesta.json()

    imagen_url = datos_pokemon['sprites']['front_default']
    peso = datos_pokemon['weight']
    tamaño = datos_pokemon['height']
    movimientos = [movimiento['move']['name'] for movimiento in datos_pokemon['moves']]
    habilidades = [habilidad['ability']['name'] for habilidad in datos_pokemon['abilities']]
    tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]

    pokemon_info = {
        'nombre': nombre_pokemon,
        'imagen': imagen_url,
        'peso': peso,
        'tamaño': tamaño,
        'movimientos': movimientos,
        'habilidades': habilidades,
        'tipos': tipos
    }

    return pokemon_info

def mostrar_informacion_pokemon(pokemon_info):
    if pokemon_info is None:
        print("Error: Pokémon no encontrado.")
        return

    print("Imagen del Pokémon:")
    print(pokemon_info['imagen'])
    print("Estadísticas del Pokémon:")
    print("Peso:", pokemon_info['peso'])
    print("Tamaño:", pokemon_info['tamaño'])
    print("Movimientos:", pokemon_info['movimientos'])
    print("Habilidades:", pokemon_info['habilidades'])
    print("Tipos:", pokemon_info['tipos'])

def guardar_info_pokemon(pokemon_info):
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')

    archivo_json = f"pokedex/{pokemon_info['nombre'].lower()}.json"
    with open(archivo_json, 'w') as archivo:
        json.dump(pokemon_info, archivo, indent=4)

def main():
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
    pokemon_info = obtener_informacion_pokemon(nombre_pokemon)
    mostrar_informacion_pokemon(pokemon_info)
    guardar_info_pokemon(pokemon_info)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

