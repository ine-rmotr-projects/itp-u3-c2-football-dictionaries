#import pprint
#from squads_data import SQUADS_DATA
#from assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):

    return_squad = {}
    squad = players_as_dictionaries(squads_list)
    
    for player in squad:
        country = player['country']
        position = player['position']
        return_squad.setdefault(country, {})
        return_squad[country].setdefault(position, [])
        return_squad[country][position].append(player)
    return return_squad