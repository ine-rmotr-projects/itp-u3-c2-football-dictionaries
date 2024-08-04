from .assignment_1 import players_as_dictionaries
def players_by_country_and_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    player_country = {}

    for player in squad:
        country = player["country"]
        position = player["position"]
        player_country.setdefault(country, {})
        player_country[country].setdefault(position, [])
        player_country[country][position].append(player)
    return player_country
