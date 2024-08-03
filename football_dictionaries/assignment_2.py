# Function to group players by position
def group_by_position(squads_data):
    position_dict = {}
    for player in squads_data:
        position = player['position']
        if position not in position_dict:
            position_dict[position] = []
        position_dict[position].append(player)
    return position_dict

# Group the data by position
grouped_by_position = group_by_position(new_squads_data)
print(grouped_by_position)
