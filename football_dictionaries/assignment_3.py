def players_by_country_and_position(squads_list):
    squads_list = players_as_dictionaries(squads_list)
    players_grouped_by_position_and_country = {}
    for position, players in squads_list.items():
        for player in players:
            country = player['country']
            if country not in players_grouped_by_position_and_country:
                players_grouped_by_position_and_country[country] = [player]
            else:
                players_grouped_by_position_and_country[country].append(player)
    return players_grouped_by_position_and_country