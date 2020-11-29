from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):
    list_of_player_dicts = players_as_dictionaries(squads_list)
    a_dict = {}
    for player in list_of_player_dicts:
    	country = player['country']
    	if country not in a_dict:
    		a_dict[country] = [player]
    	else:
    		a_dict[country].append(player)
    for key, value in a_dict.items():
    	position_dict = {}
    	for player in a_dict[key]:
    		if player['position'] not in position_dict:
    			position_dict[player['position']] = [player]
    		else:
    			position_dict[player['position']].append(player)
    	a_dict[key] = position_dict
    return a_dict

