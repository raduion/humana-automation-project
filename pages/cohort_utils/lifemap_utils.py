from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locators import CSS_SELECTORS, CARDS_XPATHS, TYPE_1_TALENTS, TYPE_0_TALENTS, \
    CSS_SELECTORS_LIFEMAP_CARDS, TYPE_0_PASSIONS, TYPE_1_PASSIONS, TYPE_0_IMPACTS, TYPE_1_IMPACTS, TYPE_1_VALUES, \
    TYPE_0_VALUES, TYPE_2_PASSIONS, TYPE_0_GOALS, TYPE_1_GOALS, TYPE_2_TALENTS, TYPE_2_IMPACTS, TYPE_2_VALUES, \
    TYPE_2_GOALS, TYPE_3_TALENTS, TYPE_3_PASSIONS, TYPE_3_IMPACTS, TYPE_3_VALUES, TYPE_3_GOALS, TYPE_4_TALENTS, \
    TYPE_4_PASSIONS, TYPE_4_IMPACTS, TYPE_4_VALUES, TYPE_4_GOALS
from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS, DATABASE_KEYS
import time

MAX_SCORE_VALUES = {
    'max_score_1': {
        'main_talents': TYPE_1_TALENTS,
        'secondary_talents': TYPE_2_TALENTS,
        'main_passions': TYPE_1_PASSIONS,
        'secondary_passions': TYPE_2_PASSIONS,
        'main_impacts': TYPE_1_IMPACTS,
        'secondary_impacts': TYPE_2_IMPACTS,
        'main_values': TYPE_1_VALUES,
        'secondary_values': TYPE_2_VALUES,
        'main_goals': TYPE_1_GOALS,
        'secondary_goals': TYPE_2_GOALS
    },
    'max_score_2': {
        'main_talents': TYPE_2_TALENTS,
        'secondary_talents': TYPE_1_TALENTS,
        'main_passions': TYPE_2_PASSIONS,
        'secondary_passions': TYPE_1_PASSIONS,
        'main_impacts': TYPE_2_IMPACTS,
        'secondary_impacts': TYPE_1_IMPACTS,
        'main_values': TYPE_2_VALUES,
        'secondary_values': TYPE_1_VALUES,
        'main_goals': TYPE_2_GOALS,
        'secondary_goals': TYPE_1_GOALS
    },
    'max_score_3': {
        'main_talents': TYPE_3_TALENTS,
        'secondary_talents': TYPE_1_TALENTS,
        'main_passions': TYPE_3_PASSIONS,
        'secondary_passions': TYPE_1_PASSIONS,
        'main_impacts': TYPE_3_IMPACTS,
        'secondary_impacts': TYPE_1_IMPACTS,
        'main_values': TYPE_3_VALUES,
        'secondary_values': TYPE_1_VALUES,
        'main_goals': TYPE_3_GOALS,
        'secondary_goals': TYPE_1_GOALS
    },
    'max_score_4': {
        'main_talents': TYPE_4_TALENTS,
        'secondary_talents': TYPE_1_TALENTS,
        'main_passions': TYPE_4_PASSIONS,
        'secondary_passions': TYPE_1_PASSIONS,
        'main_impacts': TYPE_4_IMPACTS,
        'secondary_impacts': TYPE_1_IMPACTS,
        'main_values': TYPE_4_VALUES,
        'secondary_values': TYPE_1_VALUES,
        'main_goals': TYPE_4_GOALS,
        'secondary_goals': TYPE_1_GOALS
    }
}


class LifeMapUtils:

    def __init__(self, browser):
        self.browser = browser
        self.base_element = BaseElement(browser)
        self.base_page = BasePage(browser)
        self.connect = Connect()

    # this function goes through LifeMap card sorting and selects card based on the inputted type

    def custom_score(self, main_talents, secondary_talents, main_passions, secondary_passions,
                     main_impacts, secondary_impacts, main_values, secondary_values, main_goals, secondary_goals):

        # start card sorting activity
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS['header_save'])
        # talents
        self.base_element.custom_card_selector(main_card_type=main_talents,
                                               secondary_card_type=secondary_talents,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS['header_save'])

        self.base_element.custom_card_selector(main_card_type=main_talents,
                                               secondary_card_type=secondary_talents,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        # passions
        self.base_element.custom_card_selector(main_card_type=main_passions,
                                               secondary_card_type=secondary_passions,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        self.base_element.custom_card_selector(main_card_type=main_passions,
                                               secondary_card_type=secondary_passions,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        # impacts
        self.base_element.custom_card_selector(main_card_type=main_impacts,
                                               secondary_card_type=secondary_impacts,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        self.base_element.custom_card_selector(main_card_type=main_impacts,
                                               secondary_card_type=secondary_impacts,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        # values
        self.base_element.custom_card_selector(main_card_type=main_values,
                                               secondary_card_type=secondary_values,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        self.base_element.custom_card_selector(main_card_type=main_values,
                                               secondary_card_type=secondary_values,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        # goals
        self.base_element.custom_card_selector(main_card_type=main_goals,
                                               secondary_card_type=secondary_goals,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        self.base_element.custom_card_selector(main_card_type=main_goals,
                                               secondary_card_type=secondary_goals,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])

    # this function compares trackID against expected data

    def track_id_checker(self, memberpersonalgeneratedkey, expected_track_id_value):
        user_object = self.connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db_dev'],
                                                 db_name='stars-gl-core-dev',
                                                 collection_name='members',
                                                 key=DATABASE_KEYS['memberPersonalGeneratedKey'],
                                                 unique_value=memberpersonalgeneratedkey)
        object_list = self.connect.return_objects(connection_string=DATABASE_CONNECTION_STRINGS['phi_db_dev'],
                                                  db_name='stars-gl-core-dev',
                                                  collection_name='usertracksprogresses',
                                                  key=DATABASE_KEYS['userId'],
                                                  unique_value=user_object['userId'])
        i = 0
        for x in object_list:
            if x['trackId'] == expected_track_id_value:
                i = i + 1
                print('There is {} object/s where the Track ID matches the expected value. \n expected: {} \n found: {}'
                      .format(i, expected_track_id_value, x['trackId']))
        if i == 0:
            print('\033[91m Track ID does not match expected value in any objects for the user. \033[0m')

    # this method loads a LifeMap URL

    def lifemap_url_loader(self, memberpersonalgeneratedkey):

        users_object = self.connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db_dev'],
                                                  db_name='stars-gl-core-dev',
                                                  collection_name='users',
                                                  key=DATABASE_KEYS['memberPersonalGeneratedKey'],
                                                  unique_value=memberpersonalgeneratedkey)
        token = users_object[DATABASE_KEYS['token']]

        self.base_page.load_url(subdomain='stars-lifemap-ui-dev.',
                                top_level_domain='herokuapp.com', second_level_domain='', subdirectory='/welcome?',
                                path=token, wait_element=CSS_SELECTORS["phone_input"])
        time.sleep(1)

    # this method inputs a phone number and passes Welcome page

    def lifemap_phone_inputter(self, phone_number):

        self.base_page.scroll_to_bottom()

        time.sleep(1)

        self.base_element.send_user_input(input_data=phone_number,
                                          input_field=CSS_SELECTORS["phone_input"],
                                          wait_element=CSS_SELECTORS["checkbox"])
        self.base_element.button_click(button_selector=CSS_SELECTORS["checkbox"],
                                       wait_element=CSS_SELECTORS['create_my_profile_button'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['create_my_profile_button'],
                                       wait_element=CSS_SELECTORS['footer_next'])

    # this method inputs a DOB and and reaches Survey page

    def lifemap_dob_inputter(self, month, day, year):

        self.base_page.scroll_to_bottom()
        time.sleep(1)
        self.base_element.send_user_input(input_data=month,
                                          input_field=CSS_SELECTORS["month_input"],
                                          wait_element=CSS_SELECTORS['footer_next'])
        self.base_element.send_user_input(input_data=day,
                                          input_field=CSS_SELECTORS["day_input"],
                                          wait_element=CSS_SELECTORS['footer_next'])
        self.base_element.send_user_input(input_data=year,
                                          input_field=CSS_SELECTORS["year_input"],
                                          wait_element=CSS_SELECTORS['footer_next'])
        time.sleep(1)
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS['take_a_survey'])
