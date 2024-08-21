def convert_to_dicts(squads_data):
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    return [{key: value for key, value in zip(keys, player)} for player in squads_data]
