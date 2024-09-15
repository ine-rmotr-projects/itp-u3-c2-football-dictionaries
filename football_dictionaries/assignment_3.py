def players_by_country_and_position(squads_list):
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
    by_country = {}
    
    for player in squad:
        country = player['country']
        position = player['position']
        by_country.setdefault(country,{})
        by_country[country].setdefault(position,[])
        by_country[country][position].append(player)
    return by_country
