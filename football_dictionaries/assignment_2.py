def players_by_position(squads_list):
	new_list = []
	for i in squads_list:
		new_dict = {}
		new_dict['number'] = i[0]
		new_dict['position'] = i[1]
		new_dict['name'] = i[2]
		new_dict['date_of_birth'] = i[3]
		new_dict['caps'] = i[4]
		new_dict['club'] = i[5]
		new_dict['country'] = i[6]
		new_dict['club_country'] = i[7]
		new_dict['year'] = i[8]
		new_list.append(new_dict)
	return new_list


def players_by_position(squads_list):
	new_list = []
	for i in squads_list:
		new_dict = {}
		new_dict['number'] = i[0]
		new_dict['position'] = i[1]
		new_dict['name'] = i[2]
		new_dict['date_of_birth'] = i[3]
		new_dict['caps'] = i[4]
		new_dict['club'] = i[5]
		new_dict['country'] = i[6]
		new_dict['club_country'] = i[7]
		new_dict['year'] = i[8]
		new_list.append(new_dict)
	position_dict = {}
	for i in new_list:
		for key,elem in i.items():
			if key == 'position' and elem not in position_dict:
				position_dict[elem] = {}
	for key, elem in position_dict.items():
		templist = []
		for i in new_list:
			if i['position'] == key:
				templist.append(i)
			position_dict[key] = templist
	return position_dict

def players_by_country_and_position(squads_list):
	new_list = []
	for i in squads_list:
		new_dict = {}
		new_dict['number'] = i[0]
		new_dict['position'] = i[1]
		new_dict['name'] = i[2]
		new_dict['date_of_birth'] = i[3]
		new_dict['caps'] = i[4]
		new_dict['club'] = i[5]
		new_dict['country'] = i[6]
		new_dict['club_country'] = i[7]
		new_dict['year'] = i[8]
		new_list.append(new_dict)
	country_dict = {}
	for i in pos_list:
		for key,elem in i.items():
			if key == 'country' and elem not in country_dict:
				country_dict[elem] = {}
	for key_main,elem_main in country_dict.items():
		position_dict = {}
		for i in pos_list:
			for keyplayer, elem in i.items():
				if keyplayer == 'position' and elem not in position_dict and i['country']== key_main:
					position_dict[elem] = {}
		countrylist = []
		for keycountry,elem in country_dict.items():
			for keypos,elem in position_dict.items():
				playerlist = []
				if i['country] == key_main and i['position'] == keypos:
				     playerlist.append(i)
			position_dict[keypos] = playerlist
			countrylist = position_dict
		country_dict[key_main] = countrylist
	return country_dict
