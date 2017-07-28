# Data
from football_dictionaries.squads_data import SQUADS_DATA

# Assignment 1
from football_dictionaries.assignment_1 import players_as_dictionaries
# Assignment 2
from football_dictionaries.assignment_2 import players_by_position
# Assignment 3
from football_dictionaries.assignment_3 import players_by_country_and_position


# Assignment 1
def test_assignment_1():
    result = players_as_dictionaries(SQUADS_DATA)
    assert len(result) == 14

    assert result[0] == {
        'caps': '',
        'club': 'Quilmes',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
        'name': 'Juan Botasso',
        'number': '1',
        'position': 'GK',
        'year': '1930'
    }

    assert result[1] == {
        'caps': '',
        'club': 'Boca Juniors',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1907-02-23)23 February 1907 (aged 23)',
        'name': 'Roberto Cherro',
        'number': '9',
        'position': 'FW',
        'year': '1930'
    }

    assert result[-1] == {
        'caps': '26',
        'club': 'Ulsan Hyundai',
        'club_country': 'South Korea',
        'country': 'South Korea',
        'date_of_birth': '(1988-04-14)14 April 1988 (aged 26)',
        'name': 'Kim Shin-Wook',
        'number': '-',
        'position': 'FW',
        'year': '2014'
    }


# Assignment 2
def test_assignment_2():
    result = players_by_position(SQUADS_DATA)
    assert len(result) == 3  # 3 positions

    goalkeepers = result['GK']
    assert len(goalkeepers) == 2

    assert goalkeepers[0] == {
        'caps': '',
        'club': 'Quilmes',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1908-10-23)23 October 1908 (aged 21)',
        'name': 'Juan Botasso',
        'number': '1',
        'position': 'GK',
        'year': '1930'
    }

    midfielders = result['MF']
    assert len(midfielders) == 8
    assert midfielders[0] == {
        'caps': '42',
        'club': 'Royal Beerschot AC',
        'club_country': 'Belgium',
        'country': 'Belgium',
        'date_of_birth': '(1900-10-26)26 October 1900 (aged 29)',
        'name': 'Pierre Braine',
        'number': '-',
        'position': 'MF',
        'year': '1930'
    }

    forwards = result['FW']
    assert len(forwards) == 4

    assert forwards[0] == {
        'caps': '',
        'club': 'Boca Juniors',
        'club_country': 'Argentina',
        'country': 'Argentina',
        'date_of_birth': '(1907-02-23)23 February 1907 (aged 23)',
        'name': 'Roberto Cherro',
        'number': '9',
        'position': 'FW',
        'year': '1930'
    }


# Assignment 3
def test_assignment_3():
    result = players_by_country_and_position(SQUADS_DATA)
    assert len(result) == 4

    expected_countries = ['Argentina', 'Belgium', 'Brazil', 'South Korea']
    assert list(result.keys()) == expected_countries

    # Argentina
    argentina = result['Argentina']
    assert len(argentina) == 2

    ar_goalkeepers = argentina['GK']
    ar_forwards = argentina['FW']
    assert len(ar_goalkeepers) == 1
    assert len(ar_forwards) == 1

    # Brazil

    brazil = result['Brazil']
    assert len(brazil) == 1  # Only midfielders

    br_midfielders = brazil['MF']
    assert len(br_midfielders) == 6

    assert br_midfielders[0] == {
        'caps': '29',
        'club': 'Chelsea',
        'club_country': 'England',
        'country': 'Brazil',
        'date_of_birth': '(1991-09-09)9 September 1991 (aged 22)',
        'name': 'Oscar',
        'number': '-',
        'position': 'MF',
        'year': '2010'
    }

    assert br_midfielders[-1] == {
        'caps': '5',
        'club': 'Chelsea',
        'club_country': 'England',
        'country': 'Brazil',
        'date_of_birth': '(1988-08-09)9 August 1988 (aged 25)',
        'name': 'Willian',
        'number': '-',
        'position': 'MF',
        'year': '2014'
    }
