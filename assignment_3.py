def players_by_country_and_position(squads_list):
    new_dict = {}
    for player in squads_list:
        position_dict = {}
        player_country = str(player[6])
        position = str(player[1])
        if player_country not in new_dict:
            if position not in position_dict:
                position_dict[position] = [{
                "number":player[0],
                "position":player[1],
                'name': player[2],
                'date_of_birth': player[3],
                'caps': player[4],
                'club': player[5],
                'country': player[6],
                'club_country': player[7],
                'year': player[8]
                    }]
                
                new_dict[player_country] = position_dict
                
            elif position in position_dict:
                position_dict[position].append({
                "number":player[0],
                "position":player[1],
                'name': player[2],
                'date_of_birth': player[3],
                'caps': player[4],
                'club': player[5],
                'country': player[6],
                'club_country': player[7],
                'year': player[8]
                })
                
                new_dict[player_country] = position_dict
            
        elif player_country in new_dict:
            if position not in position_dict:
                position_dict[position] = [{
                "number":player[0],
                "position":player[1],
                'name': player[2],
                'date_of_birth': player[3],
                'caps': player[4],
                'club': player[5],
                'country': player[6],
                'club_country': player[7],
                'year': player[8]
                    }]
                
                new_dict[player_country].update(position_dict)
                
            elif position in position_dict:
                position_dict[position].append({
                "number":player[0],
                "position":player[1],
                'name': player[2],
                'date_of_birth': player[3],
                'caps': player[4],
                'club': player[5],
                'country': player[6],
                'club_country': player[7],
                'year': player[8]
                })
                
                new_dict[player_country].update(position_dict)
            
    return new_dict