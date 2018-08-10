from warm_up.assignment_1 import build_user_as_dict
from warm_up.assignment_2 import transform_user_list_to_dict
from warm_up.assignment_3 import transform_multiple_users_to_dicts
from warm_up.assignment_4 import group_users_by_email_domain


def test_assignment_1():
    user_1 = build_user_as_dict('John', 'john@gmail.com', 31)
    assert user_1 == {
        'name': 'John',
        'email': 'john@gmail.com',
        'age': 31
    }

    user_1 = build_user_as_dict('Mary', 'mary@hotmail.com', 28)
    assert user_1 == {
        'name': 'Mary',
        'email': 'mary@hotmail.com',
        'age': 28
    }


def test_assignment_2():
    user_list_1 = ['John', 'john@gmail.com', 31]
    user_dict_1 = transform_user_list_to_dict(user_list_1)

    assert user_dict_1 == {
        'name': 'John',
        'email': 'john@gmail.com',
        'age': 31
    }

    user_list_2 = ['Mary', 'mary@hotmail.com', 28]
    user_dict_2 = transform_user_list_to_dict(user_list_2)

    assert user_dict_2 == {
        'name': 'Mary',
        'email': 'mary@hotmail.com',
        'age': 28
    }


def test_assignment_3():
    user_list_1 = ['John', 'john@gmail.com', 31]
    user_list_2 = ['Mary', 'mary@hotmail.com', 28]
    user_list_3 = ['Rose', 'rose@yahoo.com', 30]

    users = [
        user_list_1,
        user_list_2,
        user_list_3,
    ]  # IMPORTANT! First nested collection. This is a "list of lists"

    users_as_dict = transform_multiple_users_to_dicts(users)
    assert users_as_dict == [{
        'name': 'John',
        'email': 'john@gmail.com',
        'age': 31
    }, {
        'name': 'Mary',
        'email': 'mary@hotmail.com',
        'age': 28
    }, {
        'name': 'Rose',
        'email': 'rose@yahoo.com',
        'age': 30
    }]

def test_assignment_4():
    users = [{
        'name': 'John',
        'email': 'john@gmail.com',     # gmail
        'age': 31
    }, {
        'name': 'Mary',
        'email': 'mary@hotmail.com',   # hotmail
        'age': 28
    }, {
        'name': 'Rose',
        'email': 'rose@yahoo.com',     # yahoo
        'age': 30
    }, {
        'name': 'Jane',
        'email': 'jane@gmail.com',     # gmail
        'age': 25
    }, {
        'name': 'Dustin',
        'email': 'dustin@hotmail.com',  # hotmail
        'age': 35
    }]

    users_grouped = group_users_by_email_domain(users)
    assert users_grouped == {
        'gmail.com': [{
            'name': 'John',
            'email': 'john@gmail.com',     # gmail
            'age': 31
        }, {
            'name': 'Jane',
            'email': 'jane@gmail.com',     # gmail
            'age': 25
        }],
        'hotmail.com': [{
            'name': 'Mary',
            'email': 'mary@hotmail.com',   # hotmail
            'age': 28
        }, {
            'name': 'Dustin',
            'email': 'dustin@hotmail.com',  # hotmail
            'age': 35
        }],
        'yahoo.com': [{
            'name': 'Rose',
            'email': 'rose@yahoo.com',     # yahoo
            'age': 30
        }]
    }

    # Another test just in case
    users = [{
        'name': 'Jason',
        'email': 'jason@rmotr.com',
        'age': 61
    }]
    users_grouped = group_users_by_email_domain(users)

    assert users_grouped == {
        'rmotr.com': [{
            'name': 'Jason',
            'email': 'jason@rmotr.com',
            'age': 61
        }]
    }
