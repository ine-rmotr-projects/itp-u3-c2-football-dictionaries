#import pprint
#from squads_data import SQUADS_DATA

def players_as_dictionaries(squads_list):
    squads_return = []
    
    for player in squads_list:
        individual_player_dict = {
        'number': player[0],
        'position': player[1],
        'name': player[2],
        'date_of_birth': player[3],
        'caps': player[4],
        'club': player[5],
        'country': player[6],
        'club_country': player[7],
        'year': player[8]
        }
        squads_return.append(individual_player_dict)
    return squads_return
    
    '''
    #My solution - 
    
    ###############################################
    #testing not working under python 3.6.10 on Cloud9 or python 3.8.2 on Ubuntu 20 LTS
    ###############################################
    #(football) mariothegreat:~/environment/itp-u3-c2-football-dictionaries-1 (master) $ py.test itp-u3-c2-football-dictionaries-1/tests.py -k
    #Traceback (most recent call last):
    # File "/home/ec2-user/environment/football/bin/py.test", line 5, in <module>
    #from pytest import main
    #File "/home/ec2-user/environment/football/local/lib/python3.6/dist-packages/pytest.py", line 13, in <module>
    #from _pytest.fixtures import fixture, yield_fixture
    #File "/home/ec2-user/environment/football/local/lib/python3.6/dist-packages/_pytest/fixtures.py", line 832, in <module>
    #class FixtureFunctionMarker(object):
    #File "/home/ec2-user/environment/football/local/lib/python3.6/dist-packages/_pytest/fixtures.py", line 834, in FixtureFunctionMarker
    #params = attr.ib(convert=attr.converters.optional(tuple))
    #TypeError: attrib() got an unexpected keyword argument 'convert'
    ###############################################
    
    categories = [
        'number',
        'position',
        'name',
        'date_of_birth',
        'caps',
        'club',
        'country',
        'club_country',
        'year'
        ]
        
    for player in squads_list:
        squads_return.append(dict(zip(categories, player)))
    return squads_return


result = players_as_dictionaries(SQUADS_DATA)
pprint.pprint(result)
'''