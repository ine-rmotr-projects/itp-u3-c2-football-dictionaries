from football_dictionaries.assignment_2 import players_by_position, player_to_dictionary
def players_by_country_and_position(squads_list):
    import itertools
    new_dictionary = {}
    for key, group in itertools.groupby(squads_list, key = lambda item: item[6]):
        new_dictionary[key] = players_by_position(group)
    return new_dictionary

