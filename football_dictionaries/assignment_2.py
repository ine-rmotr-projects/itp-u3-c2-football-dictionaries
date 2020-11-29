# Data
from football_dictionaries.squads_data import SQUADS_DATA

# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):

    result = {}

    squads_dict = players_as_dictionaries(squads_list)

    for player in squads_dict:
        position = player['position']
        result.setdefault(position, [])
        result[position].append(player)

    return result