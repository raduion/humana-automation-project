from pages import utils
from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS, DATABASE_KEYS, DATABASE_DATA_TYPES
from pages.gmail.email_operations import EmailOperations
from pages.utils import Utils


def test_usertrackprogresses_entry_for_user_after_clicking_email_link(browser):
    # User loaded LifeMap from email. No progress made in the app.

    connect = Connect()
    email = EmailOperations()
    base_page = BasePage(browser)
    base_element = BaseElement(browser)
    utils = Utils()

    # 1. Reach 'usertrackprogresses' collection in Phi Db
    # Collection should have an entry for the user.

    # email_url = email.get_email_url()
    email_url = 'http://stars-lifemap-ui-dev.herokuapp.com/welcome?227b6390-57d4-4577-8dc9-1cc8674cc992'

    print(email_url)
    base_page.load_url(scheme='', subdomain=email_url,
                       top_level_domain='', second_level_domain='', subdirectory='',
                       path='', wait_element='div[id="app"]')

    # we're getting the usertracksprogresses object for user Radu 1 Ion

    usertracksprogresses_object = connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                                                        db_name='stars-gl-core-dev',
                                                        collection_name='usertracksprogresses',
                                                        key=DATABASE_KEYS['firstName'],
                                                        unique_value='Radu 1')
    print('Collection has an entry for the user')

    # 2. Reach a user object.
    # expected: User object should be populated with data.

    # we're checking if the member object has data in it

    if usertracksprogresses_object:
        print('User has a usertrackprogresses object created after reaching LifeMap')
    else:
        print('User does not have a usertrackprogresses object created after reaching LifeMap')
        raise AssertionError

    # 3. Verify the user object fields and values.
    # expected: There should be 16 fields present:
    #
    # 1. _id with an ObjectId value (e.g ObjectId("603e2b6ffa02bceb9fcf2c90")
    # 2. userId with an ObjectId value (e.g ObjectId("603e2b6efa02bceb9fcf2c82")
    # 3. trackID with a string value (e.g. 0001) - this represents the track user started
    # 4. trackName with a string value. (e.g. Lifemap Track) - this represents the track's name
    # 5. firstName with a string value (e.g. Radu 1) -  user first name
    # 6. lastName with a string value (e.g. Ion) - user's last name
    # 7. trackType with a string value (e.g. 1) - type of the track
    # 8. url with a string value (e.g. https://tinyurl.com/yd5gf8yq) - url sent in SMS reminders
    # 9. createdAt with a date value (e.g. 2021-03-08 09:42:32.638Z) - set when user lands on the LifeMap track
    # 10. updatedAt with a date value (e.g. 2021-03-08 09:42:32.651Z) - set when user progresses in the track
    # 11. __v version key with a Int32 value (e.g. 0)
    # 12. active with a boolean value (e.g. true) - set to true if user has not completed the track
    # 13. completed with a boolean value (e.g. false) - set to false if user has not completed the track
    # 14. consentedAt with a date value (e.g. 2021-03-08 09:42:31.000Z) - set when user lands in the track
    # 15. nextStepId with a string value of 0  - next sms index that the user should receive.
    # 16. previousSteps with a string value (e.g. null) - sms previously received by the user. set to null if user
    # hasn't received any

    # we're comparing the number of expected fields with the one existing in the object

    expected_keys = ['_id', 'userId', 'trackID', 'trackName', 'firstName', 'lastName', 'trackType', 'url', 'createdAt',
                     'updatedAt', '__v', 'active', 'completed', 'consentedAt', 'nextStepId', 'previousSteps']

    if len(usertracksprogresses_object) == len(expected_keys):
        print('\033[92m There are {} fields present in the user object \033[0m'.format(
            len(usertracksprogresses_object)))
    else:
        print('\033[91m There are {} fields present in the user object \033[0m'.format(
            len(usertracksprogresses_object)))
        raise AssertionError

    # we're comparing the expected data types saved in the object with the existing ones

    utils.compare_data_types(dict_object=usertracksprogresses_object,
                             key=DATABASE_KEYS['_id'],
                             data_type=DATABASE_DATA_TYPES['ObjectId'])
    utils.compare_data_types(dict_object=usertracksprogresses_object,
                             key=DATABASE_KEYS['userId'],
                             data_type=DATABASE_DATA_TYPES['ObjectId'])

    members_object = connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                                           db_name='stars-gl-core-dev',
                                           collection_name='members',
                                           key=DATABASE_KEYS['firstName'],
                                           unique_value='Radu 1')

    # we're checking to see if the user Ids match between the members and the usertracksprogresses objects

    if members_object[DATABASE_KEYS['userId']] == usertracksprogresses_object[DATABASE_KEYS['userId']]:
        print('User IDs match between members and usertracksprogresses objects')
    else:
        print('User IDs do not match between members and usertracksprogresses objects')
        raise AssertionError

    utils.compare_data_types(dict_object=usertracksprogresses_object,
                             key=DATABASE_KEYS['trackId'],
                             data_type=DATABASE_DATA_TYPES['string'])

    utils.compare_data_types(dict_object=usertracksprogresses_object,
                             key=DATABASE_KEYS['trackName'],
                             data_type=DATABASE_DATA_TYPES['string'])

    if usertracksprogresses_object[DATABASE_KEYS['trackName']] == "Lifemap Track":
        print('The correct trackName has been added: "{}"'.format(
            usertracksprogresses_object[DATABASE_KEYS['trackName']]))
    else:
        print(' Incorrect trackName has been added: "{}"'.format(
            usertracksprogresses_object[DATABASE_KEYS['trackName']]))

    # in progress
