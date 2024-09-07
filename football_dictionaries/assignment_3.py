def players_by_country_and_position(squads_list):
    country_dict = {}
    
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
        
        country = player[6]
        position = player[1]
        
        if country not in country_dict:
            country_dict[country] = {}
        
        if position not in country_dict[country]:
            country_dict[country][position] = []
        
        country_dict[country][position].append(player_dict)
    
    return country_dict

   
