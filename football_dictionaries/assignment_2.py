def players_by_position(squads_list):
    position_dict = {}
    for i in squads_list:
        for key,elem in i.items():
            if key == 'position' and elem not in position_dict:
                position_dict[elem] = {}
     for key, elem in position_dict.items():
        templist = set()
        for i in squads_list:
            if i['position'] == key:
                templist.add(i['name'])
            position_dict[key] = templist
     return position_dict
