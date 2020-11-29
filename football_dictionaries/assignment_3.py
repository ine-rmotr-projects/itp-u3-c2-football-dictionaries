# Data
from football_dictionaries.squads_data import SQUADS_DATA

# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):

    result = {}

    squads_dict = players_as_dictionaries(squads_list)

    for player in squads_dict:
        position = player['position']
        country = player['country']
        result.setdefault(country, {})

        result[country].setdefault(position, [])
        result[country][position].append(player)

    return result


