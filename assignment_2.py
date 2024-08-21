def group_by_position(players_dicts):
    grouped_by_position = {}
    for player in players_dicts:
        position = player['position']
        if position not in grouped_by_position:
            grouped_by_position[position] = []
        grouped_by_position[position].append(player)
    return grouped_by_position
