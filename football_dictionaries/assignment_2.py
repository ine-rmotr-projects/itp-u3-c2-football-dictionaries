def players_by_position(squads_list):
    final_dict={}
    for i in squads_list:
        position=i[1]
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
        final_dict.setdefault(position, [])
        final_dict[position].append(temp_dict)
    return final_dict
