# Pokemon Pokedex

## Descrição

Bem-vindo ao meu projeto Pokedex! Este projeto é parte dos meus primeiros estudos em Python e tem como objetivo explorar o consumo de APIs para coletar e exibir informações sobre Pokémons. Estou utilizando a PokeAPI como fonte de dados e, em breve, planejo evoluir este projeto para uma aplicação web usando o framework Django.

## Funcionalidade
### Consumo de API:
O projeto faz requisições à PokeAPI para obter informações detalhadas sobre Pokémons, como habilidades, formas, tipos, status, altura, peso e imagens.

### Aplicação Web (Em desenvolvimento): 
Uso de uma aplicação web com sistemas de cards de pokemons, consulta de pokemons e visualização de dados de pokemons.

### Seleção de Pokémons por usuário (em breve): 
A aplicação exibe um conjunto de Pokemons organizados por ID para o usuário, que poderá favoritar seu pokemons e adicioná-lo em sua coleção

## Como Executar

### Clone o Repositório:

"git clone https://github.com/oantoniovinicius/python-pokedex.git"

cd pokedex-python"

### Ative o ambiente virtual
Execute a seguinte sequência de comandos no CMD, Promp de Comando ou Powershell.
OBS.: É necessário ter o Python 3 ou superior instalado

1. "cd C:\Users\oneke\Documents\py\python-pokedex\pokedex"

2. "./Scripts/Activate.ps1"

3. "cd.."

### Instale as Dependências:

Certifique-se de ter o Python instalado na versão 3.1 ou superior. Instale as dependências necessárias:

"pip install requests" 

"pip install django"

Nota: No momento, o projeto está em migração para o Django e está sendo desenvolvido em ambiente virtual ativo.

O ambiente virtual 'pokedex' será ativado.

### Executar o projeto
Para executar o projeto, será necessário executar os seguintes comandos:

1. "cd pokedex_web"

2. "python manage.py runserver"

Agora que o servidor está on, segue o URL do projeto para executar no navegador: http://127.0.0.1:8000/pokemons/

## Futuras Melhorias

Este projeto está em constante evolução e algumas das próximas etapas incluem:

### Migração para Django: (Em andamento)
Planejo criar uma versão web deste projeto utilizando o framework Django, onde será possível acessar a Pokédex através de um navegador. 

### Aplicação em execução (Atualmente):
![Layout](https://github.com/oantoniovinicius/python-pokedex/blob/main/pokedex_web/pokemons/static/img/execution.gif)

### Novas Funcionalidades: 

Adicionar filtros de busca, salvar pokemons favoritos, criação de usuário, entre outras.

## Contato

Você pode me encontrar no LinkedIn (https://www.linkedin.com/in/antoniovinicius/) ou enviar um e-mail para devantoniovinicius@gmail.com.

## Licença

Este projeto está licenciado sob a MIT License.

