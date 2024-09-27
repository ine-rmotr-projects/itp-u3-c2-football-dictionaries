def players_by_position(squads_list):
    squads_list = players_as_dictionaries(squads_list)
    players_grouped_by_position = {}
    for player in squads_list:
        position = player['position']
        if position not in players_grouped_by_position:
            players_grouped_by_position[position] = [player]
        else:
            players_grouped_by_position[position].append(player)
    return players_grouped_by_position
