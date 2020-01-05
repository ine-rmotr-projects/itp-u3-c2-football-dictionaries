def player_to_dict(player):
    return {
        "number":player[0],
        "position":player[1],
        'name': player[2],
        'date_of_birth': player[3],
        'caps': player[4],
        'club': player[5],
        'country': player[6],
        'club_country': player[7],
        'year': player[8]
    }
    

def players_by_position(squads_list):
    new_dict = {}
    for player in squads_list:
        position = str(player[1])
        if position not in new_dict:
            new_dict[position] = [player_to_dict(player)]
        else:
            new_dict[position].append(player_to_dict(player))
    return new_dict
