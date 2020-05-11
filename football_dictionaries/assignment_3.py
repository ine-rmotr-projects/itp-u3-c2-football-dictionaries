def players_by_country_and_position(squads_list):
    final_dict={}
    for i in squads_list:
        position=i[1]
        country=i[6]
        value_dict= {
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
        final_dict.setdefault(country, {})
        final_dict[country].setdefault(position, [])
        final_dict[country][position].append(value_dict)
    return final_dict
