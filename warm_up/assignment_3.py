def transform_multiple_users_to_dicts(multiple_users):
    users = []
    for user in multiple_users:
        user_dict = {
            'name': user[0],
            'email': user[1],
            'age': user[2],
        }
        users.append(user_dict)
    return users
