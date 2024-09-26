def players_by_country_and_position(squads_list):
    players = {}
    for player in squads_list:
        country = player[6]
        position = player[1]
        players.setdefault(country,{})
        players[country].setdefault(position, [])
        players[country][position].append(
            {
            'number': player[0],
            'position': position,
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': country,
            'club_country': player[7],
            'year': player[8]
        })
    return players
