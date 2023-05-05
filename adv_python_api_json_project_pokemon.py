# Make 20 pokemon
# Construct their information from the API; Name, abilities, types, and weight
# Categorize your pokemon by Type

import requests, json

def ability_list(list):
    """
    Expects the index of a pokemon's abilities dictionary.
    Returns a list of the pokemon's ability names.
    """
    ability_list = []
    for i in list:
        ability_list.append(i['ability']['name'])
    return ability_list

def type_list(list):
    """
    Expects the index of a pokemon's types dictionary.
    Returns a list of the pokemon's types.
    """
    type_list = []
    for i in list:
        type_list.append(i['type']['name'])
    return type_list

def poke_dict(num):
    """Expects a pokemon's ID #. Returns a dictionary of that pokemon's characteristics."""
    # API url for all pokemon index dictionary
    all_poke_url = 'https://pokeapi.co/api/v2/pokemon'
    
    # dictionary object for all pokemon index (results key has list of pokemon)
    all_poke_index_response = requests.get(all_poke_url)
    
    # url for specific pokemon
    poke_data_url = all_poke_index_response.json()['results'][num]['url']
    
    # dictionary object for specific pokemon characteristics
    poke_response = requests.get(poke_data_url)
    
    # specific pokemon name for later use
    poke_name = all_poke_index_response.json()['results'][num]['name']

    # create dictionary with only desired characteristics
    # Name, abilities, types, and weight
    poke_dict = {
        'name': poke_name,
        'abilities': ability_list(poke_response.json()['abilities']),
        'type': type_list(poke_response.json()['types']),
        'weight': poke_response.json()['weight']
    }
    
    return poke_dict

def poke_type_dict(num):
    """
    Given a number of the first pokemon to categorize,
    returns a dictionary of pokemon sorted by type.
    """

    # create a list with first n = num pokemon using poke_dict()
    pokes_list = []
    for x in range(20):
        poke_name = poke_name = requests.get('https://pokeapi.co/api/v2/pokemon').json()['results'][x]['name']
        # pokes_dict[poke_name] = poke_dict(x)
        pokes_list.append(poke_dict(x))

    # create an empty dictionary for type categorization
    types_dict = {
        'bug': [],
        'fire': [],
        'flying': [],
        'grass': [],
        'normal': [],
        'poison': [],
        'water': [],
    }

    # categorize pokemon and add into the dictionary
    for i in pokes_list:
        if i['type'][0] == 'bug':
            types_dict['bug'].append(i)
        elif i['type'][0] == 'fire':
            types_dict['fire'].append(i)
        elif i['type'][0] == 'flying':
            types_dict['flying'].append(i)
        elif i['type'][0] == 'grass':
            types_dict['grass'].append(i)
        elif i['type'][0] == 'normal':
            types_dict['normal'].append(i)
        elif i['type'][0] == 'poison':
            types_dict['poison'].append(i)
        elif i['type'][0] == 'water':
            types_dict['water'].append(i)

    return types_dict

print(poke_type_dict(20))

# types_dict = {
#     'bug': [{'name': 'caterpie', 'abilities': ['shield-dust', 'run-away'], 'type': ['bug'], 'weight': 29},
#              {'name': 'metapod', 'abilities': ['shed-skin'], 'type': ['bug'], 'weight': 99}, 
#              {'name': 'butterfree', 'abilities': ['compound-eyes', 'tinted-lens'], 'type': ['bug', 'flying'], 'weight': 320}, 
#              {'name': 'weedle', 'abilities': ['shield-dust', 'run-away'], 'type': ['bug', 'poison'], 'weight': 32}, 
#              {'name': 'kakuna', 'abilities': ['shed-skin'], 'type': ['bug', 'poison'], 'weight': 100}, 
#              {'name': 'beedrill', 'abilities': ['swarm', 'sniper'], 'type': ['bug', 'poison'], 'weight': 295}], 
#     'fire': [{'name': 'charmander', 'abilities': ['blaze', 'solar-power'], 'type': ['fire'], 'weight': 85}, 
#              {'name': 'charmeleon', 'abilities': ['blaze', 'solar-power'], 'type': ['fire'], 'weight': 190}, 
#              {'name': 'charizard', 'abilities': ['blaze', 'solar-power'], 'type': ['fire', 'flying'], 'weight': 905}], 
#     'flying': [], 
#     'grass': [{'name': 'bulbasaur', 'abilities': ['overgrow', 'chlorophyll'], 'type': ['grass', 'poison'], 'weight': 69}, 
#               {'name': 'ivysaur', 'abilities': ['overgrow', 'chlorophyll'], 'type': ['grass', 'poison'], 'weight': 130}, 
#               {'name': 'venusaur', 'abilities': ['overgrow', 'chlorophyll'], 'type': ['grass', 'poison'], 'weight': 1000}],
#     'normal': [{'name': 'pidgey', 'abilities': ['keen-eye', 'tangled-feet', 'big-pecks'], 'type': ['normal', 'flying'], 'weight': 18},
#               {'name': 'pidgeotto', 'abilities': ['keen-eye', 'tangled-feet', 'big-pecks'], 'type': ['normal', 'flying'], 'weight': 300},
#               {'name': 'pidgeot', 'abilities': ['keen-eye', 'tangled-feet', 'big-pecks'], 'type': ['normal', 'flying'], 'weight': 395},
#               {'name': 'rattata', 'abilities': ['run-away', 'guts', 'hustle'], 'type': ['normal'], 'weight': 35},
#               {'name': 'raticate', 'abilities': ['run-away', 'guts', 'hustle'], 'type': ['normal'], 'weight': 185}],
#     'poison': [], 
#     'water': [{'name': 'squirtle', 'abilities': ['torrent', 'rain-dish'], 'type': ['water'], 'weight': 90}, 
#               {'name': 'wartortle', 'abilities': ['torrent', 'rain-dish'], 'type': ['water'], 'weight': 225}, 
#               {'name': 'blastoise', 'abilities': ['torrent', 'rain-dish'], 'type': ['water'], 'weight': 855}]
# }