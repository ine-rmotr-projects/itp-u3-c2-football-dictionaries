def players_by_country_and_position(squads_list):
    result_all = {}
    for cou in squads_list:
        country = cou[6]
        result = {}
        result_all.setdefault(country, result)
        for pos in squads_list:
            position = pos[1]
            result.setdefault(position, [])
            result[position].append(pos[2])
    return result_all
