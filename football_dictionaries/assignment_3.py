def group_by_country_and_position(players):
    country_dict = {}
    for player in players:
        country = player['country']
        position = player['position']
        if country not in country_dict:
            country_dict[country] = {}
        if position not in country_dict[country]:
            country_dict[country][position] = []
        country_dict[country][position].append(player)
    return country_dict

# Example data
players_as_dicts = convert_to_dicts(SQUADS_DATA)

# Group by country and position
grouped_by_country_and_position = group_by_country_and_position(players_as_dicts)
print(grouped_by_country_and_position)
