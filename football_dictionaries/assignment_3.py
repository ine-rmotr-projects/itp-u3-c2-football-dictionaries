# Function to group players by country and position
def group_by_country_and_position(squads_data):
    country_dict = {}
    for player in squads_data:
        country = player['country']
        position = player['position']
        
        if country not in country_dict:
            country_dict[country] = {}
        
        if position not in country_dict[country]:
            country_dict[country][position] = []
        
        country_dict[country][position].append(player)
    
    return country_dict

# Group the data by country and position
grouped_by_country_and_position = group_by_country_and_position(new_squads_data)
print(grouped_by_country_and_position)
