import requests 

def pegarHabilidades(poke):
    for i in poke['abilities']:
        print(i['ability']['name'])



def main():
    api = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    res = requests.get(api)
    poke = res.json()
    pegarHabilidades(poke)

if __name__ == "__main__":
    main()