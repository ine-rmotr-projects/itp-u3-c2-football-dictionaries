def player_to_dictionary(player):
    return {
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


def players_by_position(squads_list):
    pass
    new_list = {}
    for player in squads_list:
        position = str(player[1])
        if position not in new_list:
            new_list[position] = [player_to_dictionary(player)]
        else:
            new_list[position].append(player_to_dictionary(player))
    return new_list
