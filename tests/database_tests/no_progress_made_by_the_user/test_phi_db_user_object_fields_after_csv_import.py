from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS, \
    DATABASE_DATA_TYPES, DATABASE_KEYS
from pages.utils import Utils


def test_phi_db_user_object_fields_after_csv_import():
    # CSV with user data should be imported imported in PHI DB

    connect = Connect()
    utils = Utils()

    # 1. Reach 'Users' collection in PHI Db.
    # expected results: Collection should be populated with data.

    users_collection = connect.return_documents(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                                                db_name='stars-gl-core-dev',
                                                collection_name='users')
    if users_collection:
        print('Collection is populated with data')
    else:
        print('Collection is empty')

    # 2. Reach a user object.
    # expected results: User object should be populated with data.

    # we're getting the user object for user Radu 1 Ion

    member_object = connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                                          db_name='stars-gl-core-dev',
                                          collection_name='members',
                                          key=DATABASE_KEYS['firstName'],
                                          unique_value='Radu 1')

    user_id = member_object['userId']

    user_object = connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                                        db_name='stars-gl-core-dev',
                                        collection_name='users',
                                        key=DATABASE_KEYS['_id'],
                                        unique_value=user_id)

    # we're checking if the user object has data in it

    if user_object:
        print('User object is populated with data')
    else:
        print('User object is empty')

    # 3. Verify the user object fields and values.
    # expected results: There should be 9 fields present:
    #
    # 1. _id with an ObjectId value (e.g ObjectId("603e2b6dfa02bceb9fcf2c79")
    # 2. memberPersonalGeneratedKey with a string value (e.g. 2975043039904)
    # 3. token with a string value (e.g. 65f8a87f-77d0-4efb-92f5-251c29fcddc1)
    # 4. emailToken with a string value (e.g. 41b372cd-3260-4f31-9468-0014f73793ef)
    # 5. synced with a boolean value (e.g. true)
    # 6. createdAt with a date value (e.g. 2021-03-02 12:11:25.871Z)
    # 7. updatedAt with a date value (e.g. 2021-03-02 12:12:02.181Z)
    # 8. __v version key with a Int32 value (e.g. 0)
    # 9. exportUpdatedAt with a date value (e.g. 2021-03-02 12:11:30.345Z)

    expected_keys = ['_id', 'memberPersonalGeneratedKey', 'token', 'emailToken', 'synced', 'createdAt', 'updatedAt',
                     '__v', 'exportUpdatedAt']

    # we're comparing the number of expected fields with the one existing in the object

    if len(user_object) == len(expected_keys):
        print('\033[92m There are {} fields present in the user object \033[0m'.format(len(user_object)))
    else:
        print('\033[91m There are {} fields present in the user object \033[0m'.format(len(user_object)))

    # we're checking if all the expected keys are present

    user_object_keys = user_object.keys()

    for i in expected_keys:
        if i in user_object_keys:
            print('\033[92m {} key was found in the user object \033[0m'.format(i))
        else:
            print('\033[91m {} key not found in the user object \033[0m'.format(i))

    # we're comparing the expected data types saved in the object with the existing ones. at this moment we don't need
    # the actual values

    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['_id'],
                             data_type=DATABASE_DATA_TYPES['ObjectId'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['memberPersonalGeneratedKey'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['token'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['emailToken'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['synced'],
                             data_type=DATABASE_DATA_TYPES['boolean'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['createdAt'],
                             data_type=DATABASE_DATA_TYPES['date'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['updatedAt'],
                             data_type=DATABASE_DATA_TYPES['date'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['__v'],
                             data_type=DATABASE_DATA_TYPES['int'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['exportUpdatedAt'],
                             data_type=DATABASE_DATA_TYPES['date'])
