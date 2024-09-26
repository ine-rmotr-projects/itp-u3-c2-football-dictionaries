def players_by_position(squads_list):
    players = {}
    for player in squads_list:
        position = player[1]
        players.setdefault(position,[])
        players[position].append(
            {
            'number': player[0],
            'position': position,
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
        })
    return players
