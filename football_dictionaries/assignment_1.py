def players_as_dictionaries(squads_list):
    result = []
    for squad_member in squads_list:
        result.append({
                'number': squad_member[0],
		'position': squad_member[1],
                'name': squad_member[2],
                'date_of_birth': squad_member[3],
                'caps': squad_member[4],
                'club': squad_member[5],
                'country': squad_member[6],
                'club_country': squad_member[7],
                'year': squad_member[8]})
    return result
