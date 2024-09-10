from django.shortcuts import render
import requests
from django.core.paginator import Paginator

pokemon_cache = {}

def getPokemonInfo(pokemon_name):
    if pokemon_name in pokemon_cache:
        return pokemon_cache[pokemon_name]
    
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    res = requests.get(api)

    if res.status_code == 200:
        poke = res.json()
        
        abilities = [i['ability']['name'] for i in poke['abilities']]
        type = [i['type']['name'] for i in poke['types']]
        stats = [f"{i['stat']['name']}: {i['base_stat']}" for i in poke['stats']]
        image_url = poke['sprites']['front_default'] 
        pokemon_id = poke['id']

        pokemon_data = {
            'name': poke['name'],
            'abilities': abilities,
            'type': type,
            'stats': stats,
            'image_url': image_url,  
            'id': pokemon_id
        }
        
        pokemon_cache[pokemon_name] = pokemon_data
        return pokemon_data
    
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

def pokemonList(request):
    query = request.GET.get('query')
    pokemons = []
    pokemon_type = request.GET.get('type')
    page_number = int(request.GET.get('page', 1))

    if pokemon_type:
        pokemon_names = getPokemonsByType(pokemon_type.lower())  
    else:
        pokemon_names = getAllPokemons() 

    if query:
        pokemons = searchPokemons(query.lower(), pokemon_names)
    else:
        paginator = Paginator(pokemon_names, 24) 
        page_obj = paginator.get_page(page_number)
        for pokemon_name in page_obj:  
            pokemon_info = getPokemonInfo(pokemon_name)
            if pokemon_info:
                pokemons.append(pokemon_info)
                
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'pokemon_list_partial.html', {'pokemons': pokemons})
                
    context = {
        'pokemons': pokemons
    }

    return render(request, 'pokemon_list.html', context)

def searchPokemons(prefix, pokemon_names):
    matched_pokemons = []

    for pokemon_name in pokemon_names:
        if pokemon_name.startswith(prefix):
            pokemon_info = getPokemonInfo(pokemon_name)
            if pokemon_info:
                matched_pokemons.append(pokemon_info)
    
    return matched_pokemons     

def getPokemonsByType(pokemon_type):
    api = f'https://pokeapi.co/api/v2/type/{pokemon_type}'
    res = requests.get(api)
    
    if res.status_code == 200:
        type_data = res.json()
        pokemon_names = [poke['pokemon']['name'] for poke in type_data['pokemon']]
        return pokemon_names
    else:
        return []