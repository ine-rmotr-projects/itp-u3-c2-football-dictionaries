def players_by_position(squads_list):
    players_as_dictionaries = []
    for player in squads_list:
        players_dict = {
        'caps' : player[4],
        'club': player[5],
        'club_country': player[7],
        'country': player[6],
        'date_of_birth': player[3],
        'name': player[2],
        'number' : player[0],
        'position': player[1],
        'year': player[8]
        }
        players_as_dictionaries.append(players_dict)
    


    squad = players_as_dictionaries
    by_position = {}
    
    for player in squad:
        position = player['position']
        by_position.setdefault(position,[])
        by_position[position].append(player)
        
    return by_position
