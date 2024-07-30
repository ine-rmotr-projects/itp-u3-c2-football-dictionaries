def transform_list_player_to_dict(player_as_list):
  player_as_dict={
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

def players_by_position(squads_list):
  players = {}
  for player_as_list in squads_list:
    player= transform_list_player_to_dict(player_as_list)
    position=player['position'] #GK


    #if position not in players:
      #players[position]=[]

    players.setdefault(position,[])

# players[position].append(player)
    list_by_position= players.get(position)
    list_by_position.append(player)
  return players
