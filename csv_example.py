import csv


def read_squad_file(file_name='squads.csv'):
    squad = []
    with open(file_name) as fp:
        reader = csv.reader(fp)
        for line in reader:
            squad.append(line)

    return squad
