import random
import requests 

def printInfo(pokemon_info):
    if pokemon_info:
        info = {
            "Pokémon": pokemon_info['name'],
            "Habilidades": ", ".join(pokemon_info['abilities']),
            "Formas": ", ".join(pokemon_info['forms']),
            "Tipo": ", ".join(pokemon_info['type']),
            "Status": ", ".join(pokemon_info['stats']),
            "Altura": pokemon_info['height'],
            "Peso": pokemon_info['weight']
        }
        for key, value in info.items():
            print(f"{key}: {value}")
        print("\n")

def getPokemonInfo(pokemon_name):
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    res = requests.get(api)

    if res.status_code == 200:
        poke = res.json()
        
        abilities = [i['ability']['name'] for i in poke['abilities']]
        forms = [i['name'] for i in poke['forms']]
        type = [i['type']['name'] for i in poke['types']]
        stats = [f"{i['stat']['name']}: {i['base_stat']}" for i in poke['stats']]
        height = poke['height']
        weight = poke['weight']

        return {
            'name': pokemon_name,
            'abilities': abilities,
            'forms': forms,
            'type': type,
            'stats': stats,
            'height': height,
            'weight': weight
        }
       
    else:
        print("Falha ao acessar a API. Código de status:", res.status_code)

def getAllPokemons():
    api = 'https://pokeapi.co/api/v2/pokemon?limit=1000'  
    res = requests.get(api)
    if res.status_code == 200:
        data = res.json()
        return [pokemon['name'] for pokemon in data['results']]
    else:
        print("Falha ao acessar a lista de Pokémons. Código de status:", res.status_code)
        return []

def main():
    allPokemons = getAllPokemons()
    if allPokemons:
        randomPokemons = random.sample(allPokemons, 5)  # Seleciona 5 Pokémons aleatórios
        for pokemon in randomPokemons:
            pokemon_info = getPokemonInfo(pokemon)
            printInfo(pokemon_info)
    else:
        print("Não foi possível obter a lista de Pokémons.")
    
    
if __name__ == "__main__":
    main()