def players_as_dictionaries(squads_list):
    list_of_dicts = []
    for player in squads_list:
    	a_dict = {}
    	a_dict['number'] = player[0]
    	a_dict['position'] = player[1]
    	a_dict['name'] = player[2]
    	a_dict['date_of_birth'] = player[3]
    	a_dict['caps'] = player[4]
    	a_dict['club'] = player[5]
    	a_dict['country'] = player[6]
    	a_dict['club_country'] = player[7]
    	a_dict['year'] = player[8]
    	list_of_dicts.append(a_dict)
    return list_of_dicts