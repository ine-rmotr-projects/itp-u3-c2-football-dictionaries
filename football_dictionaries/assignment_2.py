def players_by_position(squads_list):
    player_dict = players_as_dictionaries(squads_list)
    position_dict = {}
    for player in player_dict:
        position = player['position']
        position_dict.setdefault(position, [])
        position_dict[position].append(player)
    return position_dict
