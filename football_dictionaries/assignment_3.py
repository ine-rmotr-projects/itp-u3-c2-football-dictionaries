def players_by_country_and_position(squads_list):
    player_dict = players_by_position(squads_list)
    country_dict = {}
    for position, player in player_dict.items():
        for profiles in player:
            country = profiles['country']
            country_dict.setdefault(country, {})
            country_dict[country].setdefault(position, [])
            country_dict[country][position].append(profiles)
    return country_dict

