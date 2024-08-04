def players_as_dictionaries(squads_data):
    keys = [
        'number', 'position', 'name', 'date_of_birth', 
        'caps', 'club', 'country', 'club_country', 'year'
    ]
    players_dict_list = []

    for player_data in squads_data:
        player_dict = dict(zip(keys, player_data))
        players_dict_list.append(player_dict)

    return players_dict_list
