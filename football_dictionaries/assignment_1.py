def players_as_dictionaries(squads_list):
    final_list=[]
    for i in squads_list:
        temp_dict= {
            'number': i[0],
            'position': i[1],
            'name': i[2],
            'date_of_birth': i[3],
            'caps': i[4],
            'club': i[5],
            'country': i[6],
            'club_country': i[7],
            'year': i[8]
            }
        final_list.append(temp_dict)
    return final_list
