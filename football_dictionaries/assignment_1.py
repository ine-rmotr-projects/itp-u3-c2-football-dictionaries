def players_as_dictionaries(squads_list):
    new_list = []
    for i in squads_list:
        new_dict = {}
        new_dict['number'] = i[0]
        new_dict['position'] = i[1]

        new_dict['name'] = i[2]

        new_dict['date of birth'] = i[3]

        new_dict['caps'] = i[4]

        new_dict['club'] = i[5]

        new_dict['country'] = i[6]

        new_dict['club country'] = i[7]

        new_dict['year'] = i[8]
        new_list.append(new_dict)
    return new_list


