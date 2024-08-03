# Initial list of players
SQUADS_DATA = [
    [
        "1", "GK", "Juan Botasso", "(1908-10-23)23 October 1908 (aged 21)", "", 
        "Quilmes", "Argentina", "Argentina", "1930"
    ],
    [
        "9", "FW", "Roberto Cherro", "(1907-02-23)23 February 1907 (aged 23)", "", 
        "Boca Juniors", "Argentina", "Argentina", "1930"
    ]
    # More Players...
]

# Define the keys for the dictionary
keys = [
    'number', 'position', 'name', 'date_of_birth', 'caps', 
    'club', 'country', 'club_country', 'year'
]

# Function to convert list of lists to list of dictionaries
def lists_to_dicts(squads_data):
    return [dict(zip(keys, player)) for player in squads_data]

# Convert the data
new_squads_data = lists_to_dicts(SQUADS_DATA)
print(new_squads_data)
    
