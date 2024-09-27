
def players_as_dictionaries(squads_list):
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    detailed_squad = []
    for player in squads_list:
        squads_dict = {}
        for position, value in enumerate(player):
            squads_dict[keys[position]] = value
        detailed_squad.append(squads_dict)
    return detailed_squad