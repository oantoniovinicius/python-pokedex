from django.shortcuts import render
import requests

def getPokemonInfo(pokemon_id):
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    res = requests.get(api)

    if res.status_code == 200:
        poke = res.json()
        
        abilities = [i['ability']['name'] for i in poke['abilities']]
        #forms = [i['name'] for i in poke['forms']]
        type = [i['type']['name'] for i in poke['types']]
        stats = [f"{i['stat']['name']}: {i['base_stat']}" for i in poke['stats']]
        image_url = poke['sprites']['front_default'] 
        pokemon_id = poke['id']

        return {
            'name': poke['name'],
            'abilities': abilities,
            #'forms': forms,
            'type': type,
            'stats': stats,
            'image_url': image_url,  
            'id': pokemon_id
        }
    
    else:
        return None

def getAllPokemons():
    api = 'https://pokeapi.co/api/v2/pokemon?limit=1000'  
    res = requests.get(api)
    if res.status_code == 200:
        data = res.json()
        return [pokemon['name'] for pokemon in data['results']]
    else:
        return []

def pokemon_list(request):
    query = request.GET.get('query')
    pokemons = []

    if query:
        pokemons = searchPokemons(query.lower())
    else:
        for pokemon_id in range(1, 19):
            pokemon_info = getPokemonInfo(pokemon_id)
            if pokemon_info:
                pokemons.append(pokemon_info)
    
    context = {
        'pokemons': pokemons
    }

    return render(request, 'pokemon_list.html', context)

def searchPokemons(prefix):
    allPokemons = getAllPokemons()
    matched_pokemons = []

    for pokemon_name in allPokemons:
        if pokemon_name.startswith(prefix):
            pokemon_info = getPokemonInfo(pokemon_name)
            if pokemon_info:
                matched_pokemons.append(pokemon_info)
    
    return matched_pokemons          
