# assignment_1.py
# William Ponton 1.16.21
# Football Dictionaries Project


# players_as_dictionaries(list)
# takes an input of list of lists and converts to a list of dictionaries
def players_as_dictionaries(squads_list):
    squad_dict = []
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
            'year': player[8],
            }
        player_dict.append(player_dict)
    return squad_dict
