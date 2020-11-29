from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    list_of_player_dicts = players_as_dictionaries(squads_list)
    position_dict = {}
    for player in list_of_player_dicts:
    	if player['position'] not in position_dict:
    		position_dict[player['position']] = [player]
    	else:
    		position_dict[player['position']].append(player)
    return position_dict