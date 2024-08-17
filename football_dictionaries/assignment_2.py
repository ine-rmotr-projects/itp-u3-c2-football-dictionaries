def players_by_position(squads_list):
    positions = {}
    for player in squads_list:
        if player[1] not in positions:
            positions[player[1]] = []
    for player in squads_list:
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
        }
        position = player[1]
        positions[position].append(player_dict)
    return positions
