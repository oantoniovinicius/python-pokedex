import requests 

def pegarHabilidades(poke):
    habilidades = []
    for i in poke['abilities']:
        habilidades.append(i['ability']['name'])
    return habilidades

def pegarFormas(poke):
    formas = []
    for i in poke['forms']:
        formas.append(i['name'])
    return formas

def pegarTipo(poke):
    tipo = []
    for i in poke['types']:
        tipo.append(i['type']['name'])
    return tipo

def getStats(poke):
    stats = []
    for i in poke['stats']:
        nome = i['stat']['name']
        valor = i['base_stat'] 
        stats.append(f"{nome}: {valor}")
    return stats

def printInfo(pokemon_name, abilities, forms, type, stats):
    info = {
        "Pokémon": pokemon_name,
        "Habilidades": ", ".join(abilities),
        "Formas": ", ".join(forms),
        "Tipo": ", ".join(type),
        "Status": ", ".join(stats)
    }
    for key, value in info.items():
        print(f"{key}: {value}")

def main():
    api = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    res = requests.get(api)
    
    if res.status_code == 200:
        poke = res.json()
        
        abilities = pegarHabilidades(poke)
        forms = pegarFormas(poke)
        type = pegarTipo(poke)
        stats = getStats(poke)

        print("Nome:", "[Pikachu]", "\nHabilidades:", abilities,"\nForma:", forms, "\nTipo:", type, "\nStatus:", stats)
    else:
        print("Falha ao acessar a API. Código de status:", res.status_code)

if __name__ == "__main__":
    main()