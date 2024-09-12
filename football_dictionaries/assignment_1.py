def players_as_dictionaries(squads_list):
    final_list=[]
    for i in squads_list:
        temp_dict= {
            'number': i[0],
            'position': i[1],
            'name': i[2],
            'date_of_birth': i[3],
            'caps': i[4],
            'club': i[5],
            'country': i[6],
            'club_country': i[7],
            'year': i[8]
            }
        final_list.append(temp_dict)
    return final_list

'''import csv
def read_squad_file(file_name='squads.csv'):
    squad = []
    with open(file_name, encoding='utf-8') as fp:
        reader = csv.reader(fp)
        for line in reader:
            squad.append(line)

    return squad

list_squad=read_squad_file(file_name='squads.csv')
'''
'''
assignment1=players_as_dictionaries(list_squad)
print(assignment1[0])
'''
