def players_by_position(squads_list):
    result = {}
    for pos in squads_list:
        position = pos[1]
        result.setdefault(position, [])
        result[position].append(pos[2])
    return result
