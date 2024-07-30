def transform_list_player_to_dict(player_as_list):
    player_as_dict = {
        'caps': player_as_list[4],
        'club': player_as_list[5],
        'club_country': player_as_list[7],
        'country': player_as_list[6],
        'date_of_birth': player_as_list[3],
        'name': player_as_list[2],
        'number': player_as_list[0],
        'position': player_as_list[1],
        'year': player_as_list[8],
    }
    return player_as_dict

def players_by_country_and_position(squads_list):
    players = {}
    for player_as_list in squads_list:
        player = transform_list_player_to_dict(player_as_list)
        country = player['country']
        position = player['position']
        
        if country not in players:
            players[country] = {}
        
        if position not in players[country]:
            players[country][position] = []

        players[country][position].append(player)
    
    return players


