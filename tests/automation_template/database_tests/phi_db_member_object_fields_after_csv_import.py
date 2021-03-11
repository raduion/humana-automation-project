from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS, \
    DATABASE_DATA_TYPES, DATABASE_KEYS
from pages.utils import Utils


def test_phi_db_user_object_fields_after_csv_import():
    # CSV with user data should be imported imported in PHI DB

    connect = Connect()
    utils = Utils()

    # 1. Reach 'Members' collection in PHI Db
    # expected results: Collection should be populated with data.

    users_collection = connect.return_documents(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                                                db_name='stars-gl-core-dev',
                                                collection_name='members')
    if users_collection:
        print('Collection is populated with data')
    else:
        print('Collection is empty')

    # 2. Reach a member object.
    # expected results: Member object should be populated with data.

    # we're getting the member object for user Radu 1 Ion

    member_object = connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                                          db_name='stars-gl-core-dev',
                                          collection_name='members',
                                          key='firstName',
                                          unique_value='Radu 1')

    # we're checking if the member object has data in it

    if member_object:
        print('Member object is populated with data')
    else:
        print('Member object is empty')

    # 3. Verify the member object fields and values.
    # expected results: There should be 23 fields present:
    #
    # 1. _id with an ObjectId value (e.g ObjectId("603e2b6ffa02bceb9fcf2c90")
    # 2. userTracks with an array value containg no elements (e.g. [0 elements])
    # 3. memberPersonalGeneratedKey with a string value (e.g. 8296904340771)
    # 4. userId with an ObjectId value (e.g ObjectId("603e2b6efa02bceb9fcf2c82")
    # 5. lastName with a string value - member last name (e.g Ion)
    # 6. firstName with a string value - member first name (e.g Radu)
    # 7. cardId with a string value - member card ID (e.g. Z1118963600)
    # 8. addressLine1 with a string value - member adress (e.g. 184MEMBER ADDRESS LINE 1)
    # 9. addressLine2 with a string value - member adress (e.g. MEMBER ADDRESS LINE 2)
    # 10. cityName with a string value - member city (e.g ODEMEMBER CITY)
    # 11. stateCode with a string value - member state code (e.g. ST)
    # 12. zipCode with a string value - member zip code (e.g. 60400)
    # 13. birthDate with a date value - member birthdate (e.g. 1949-04-11 00:00:00.000Z)
    # 14. phoneNumber  with a string value - member phone number (e.g. 5555556741)
    # 15. customerId with a string value (e.g. 259658)
    # 16. languageSpokenCode with an empty? value
    # 17. sexCode with a string value - member sex (e.g F)
    # 18. email with a string value - member email (e.g. humana.automation@gmail.com)
    # 19. group with a string value (e.g. STATE OF KENTUCKY)
    # 20. smoker with a string value (e.g N)
    # 21. createdAt with a date value (e.g. 2021-03-02 12:11:27.065Z)
    # 22. updatedAt with a date value (e.g. 2021-03-02 12:11:27.065Z)
    # 23. __v version key with a Int32 value (e.g. 0)

    expected_keys = ['_id', 'userTracks', 'memberPersonalGeneratedKey', 'userId', 'lastName', 'firstName', 'cardId',
                     'addressLine1', 'addressLine2', 'cityName', 'stateCode', 'zipCode', 'birthDate', 'phoneNumber',
                     'customerId', 'languageSpokenCode', 'sexCode', 'email', 'group', 'smoker', 'createdAt',
                     'updatedAt', '__v']

    # we're comparing the number of expected fields with the one existing in the object

    if len(member_object) == len(expected_keys):
        print('\033[92m There are {} fields present in the user object \033[0m'.format(len(member_object)))
    else:
        print('\033[91m There are {} fields present in the user object \033[0m'.format(len(member_object)))

    # we're checking if all the expected keys are present

    member_object_keys = member_object.keys()

    for i in expected_keys:
        if i in member_object_keys:
            print('\033[92m {} key was found in the user object \033[0m'.format(i))
        else:
            print('\033[91m {} key not found in the user object \033[0m'.format(i))

    # we're comparing the expected data types saved in the object with the existing ones. at this moment we don't need
    # the actual values

    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['_id'],
                             data_type=DATABASE_DATA_TYPES['ObjectId'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['userTracks'],
                             data_type=DATABASE_DATA_TYPES['array'])

    # at this point usertracks should be empty

    if not member_object[DATABASE_KEYS['userTracks']]:
        print('List does not contain any elements before reaching a track')
    else:
        print('List contains elements before reaching a track')

    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['memberPersonalGeneratedKey'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['userId'],
                             data_type=DATABASE_DATA_TYPES['ObjectId'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['lastName'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['firstName'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['cardId'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['addressLine1'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['addressLine2'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['cityName'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['stateCode'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['zipCode'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['birthDate'],
                             data_type=DATABASE_DATA_TYPES['date'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['phoneNumber'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['customerId'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['languageSpokenCode'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['sexCode'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['email'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['group'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['smoker'],
                             data_type=DATABASE_DATA_TYPES['string'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['createdAt'],
                             data_type=DATABASE_DATA_TYPES['date'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['updatedAt'],
                             data_type=DATABASE_DATA_TYPES['date'])
    utils.compare_data_types(dict_object=member_object,
                             key=DATABASE_KEYS['__v'],
                             data_type=DATABASE_DATA_TYPES['int'])
