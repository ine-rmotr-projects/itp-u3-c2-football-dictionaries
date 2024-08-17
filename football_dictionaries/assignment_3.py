def players_by_country_and_position(squads_list):
    countries = {}

    for player in squads_list:
        country = player[6]  
        position = player[1]  
        if country not in countries:
            countries[country] = {}
        if position not in countries[country]:
            countries[country][position] = []
            
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
        
        countries[country][position].append(player_dict)
    return countries
