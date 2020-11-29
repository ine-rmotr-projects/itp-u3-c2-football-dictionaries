#import pprint
#from squads_data import SQUADS_DATA
#from assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    return_position = {}
    squad = players_as_dictionaries(squads_list)

    for player in squad:
      position = player['position']
      return_position.setdefault(position, [])
      return_position[position].append(player)
      
    return return_position