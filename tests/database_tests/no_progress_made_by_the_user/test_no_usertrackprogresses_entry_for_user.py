from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS


def test_no_usertrackprogresses_entry_for_user():
    # User did not load LifeMap. No progress made in the app.

    connect = Connect()

    # 1. Reach 'usertrackprogresses' collection in Phi Db
    # Collection should not have any data for the user

    # we're getting the usertracksprogresses object for user Radu 1 Ion
    print(DATABASE_CONNECTION_STRINGS['phi_db_dev'])

    member_object = connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db_dev'],
                                          db_name='stars-gl-core-dev',
                                          collection_name='usertracksprogresses',
                                          key='firstName',
                                          unique_value='Radu 1')

    # we're checking if the member object has data in it

    if not member_object:
        print('User does not have a usertrackprogresses object created before reaching LifeMap')
    else:
        print('User has a usertrackprogresses object created before reaching LifeMap')
        raise AssertionError

