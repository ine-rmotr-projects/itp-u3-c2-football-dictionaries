
from .assignment_1 import players_as_dictionaries
def players_by_position(squads_data):
    players_by_position = {}
    players_dict_list = players_as_dictionaries(squads_data)

    for player in players_dict_list:
        position = player['position']
        if position not in players_by_position:
            players_by_position[position] = []
        players_by_position[position].append(player)

    return players_by_position
