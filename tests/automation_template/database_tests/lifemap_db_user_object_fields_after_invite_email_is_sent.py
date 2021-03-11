from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS, \
    DATABASE_DATA_TYPES, DATABASE_KEYS
from pages.utils import Utils


def test_lifemap_db_user_object_fields_after_invite_email_is_sent():
    # Invite Email sent. Object is created when the emails are sent

    connect = Connect()
    utils = Utils()

    # 1. Reach 'users' collection in LifeMap Db.
    # expected results: Collection should be populated with data.

    users_collection = connect.return_documents(connection_string=DATABASE_CONNECTION_STRINGS['lifemap_db'],
                                                db_name='stars-lm-dev',
                                                collection_name='users')
    if users_collection:
        print('Collection is populated with data')
    else:
        print('Collection is empty')

    # 2. Reach a user object.
    # expected results: User object should be populated with data.

    # we're getting the user object for user Radu 1

    user_object = connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['lifemap_db'],
                                        db_name='stars-lm-dev',
                                        collection_name='users',
                                        key=DATABASE_KEYS['firstName'],
                                        unique_value='Radu 1')

    # we're checking if the user object has data in it

    if user_object:
        print('User object is populated with data')
    else:
        print('User object is empty')

    # 3. Verify the user object fields and values.
    # expected results: There should be 10 fields present:
    #
    # 1. _id with an ObjectId value (e.g ObjectId("603e2b6ffa02bceb9fcf2c90")
    # 2. userId with an string value (e.g 604a252880162a5838976e74)
    # 3. token with a string value (e.g. 3367fa95-c961-4deb-b2bd-6ec83f329010)
    # 4. emailToken with a string value - used in email for autologin (e.g. ade2f1ec-fb33-4a70-b89a-3b1145c354c1)
    # 5. birthDate with a date value - user birthdate (e.g. 1949-04-11 00:00:00.000Z)
    # 6. firstName with a string value -  user first name (e.g. Radu 1)
    # 7. group with a string value (e.g. STATE OF KENTUCKY)
    # 8. createdAt with a date value (e.g. 2021-03-02 12:11:27.065Z)
    # 9. updatedAt with a date value (e.g. 2021-03-02 12:11:27.065Z)
    # 10. __v version key with a Int32 value (e.g. 0)

    expected_keys = ['_id', 'userId', 'token', 'emailToken', 'birthDate', 'firstName', 'group',
                     'createdAt', 'updatedAt', '__v']

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
                             key=DATABASE_KEYS['userId'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['token'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['emailToken'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['birthDate'],
                             data_type=DATABASE_DATA_TYPES['date'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['firstName'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['group'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['createdAt'],
                             data_type=DATABASE_DATA_TYPES['date'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['updatedAt'],
                             data_type=DATABASE_DATA_TYPES['date'])
    utils.compare_data_types(dict_object=user_object,
                             key=DATABASE_KEYS['__v'],
                             data_type=DATABASE_DATA_TYPES['int'])
