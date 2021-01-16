# assignment_2.py
# William Ponton 1.16.21
# Football Dictionaries Project

# Import packages
from .assignment_1 import players_as_dictionaries

# players_by_position
# groups players by their position
def players_by_position(squads_list):
    player_position = {}
    squad = players_as_dictionaries(squads_list)

    for player in squad:
        position = player["position"]
        # setdefault by position
        player_position.setdefault(position, [])
        player_position[position].append(player)
    return player_position