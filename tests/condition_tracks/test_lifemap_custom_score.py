import time

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locators import CSS_SELECTORS, CARDS_XPATHS, TYPE_1, TYPE_0, TYPE_1_TALENTS, TYPE_0_TALENTS, \
    CSS_SELECTORS_LIFEMAP_CARDS, TYPE_0_PASSIONS, TYPE_1_PASSIONS, TYPE_0_IMPACTS, TYPE_1_IMPACTS, TYPE_1_VALUES, \
    TYPE_0_VALUES, TYPE_2_PASSIONS, TYPE_0_GOALS, TYPE_1_GOALS, TYPE_2_TALENTS, TYPE_2_IMPACTS, TYPE_2_VALUES, \
    TYPE_2_GOALS
from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS, DATABASE_KEYS
from pages.custom_score_lifemap import CustomLifemapScore


def test_lifemap_script(browser):
    connect = Connect()
    base_element = BaseElement(browser)
    base_page = BasePage(browser)
    custom_score = CustomLifemapScore(browser, base_element)

    users_object = connect.return_object(connection_string=DATABASE_CONNECTION_STRINGS['phi_db_dev'],
                                         db_name='stars-gl-core-dev',
                                         collection_name='users',
                                         key=DATABASE_KEYS['memberPersonalGeneratedKey'],
                                         unique_value='1000000000013')
    token = users_object[DATABASE_KEYS['token']]

    base_page.load_url(subdomain='stars-lifemap-ui-dev.',
                       top_level_domain='herokuapp.com', second_level_domain='', subdirectory='/welcome?',
                       path=token, wait_element=CSS_SELECTORS["phone_input"])

    base_page.scroll_to_bottom()
    time.sleep(1)
    base_element.send_user_input(input_data='1234567890',
                                 input_field=CSS_SELECTORS["phone_input"],
                                 wait_element=CSS_SELECTORS["checkbox"])
    base_element.button_click(button_selector=CSS_SELECTORS["checkbox"],
                              wait_element=CSS_SELECTORS['create_my_profile_button'])
    base_element.button_click(button_selector=CSS_SELECTORS['create_my_profile_button'],
                              wait_element=CSS_SELECTORS['footer_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                              wait_element=CSS_SELECTORS['header_save'])

    custom_score.custom_score(main_talents=TYPE_1_TALENTS,
                              secondary_talents=TYPE_2_TALENTS,
                              main_passions=TYPE_1_PASSIONS,
                              secondary_passions=TYPE_2_PASSIONS,
                              main_impacts=TYPE_1_IMPACTS,
                              secondary_impacts=TYPE_2_IMPACTS,
                              main_values=TYPE_1_VALUES,
                              secondary_values=TYPE_2_VALUES,
                              main_goals=TYPE_1_GOALS,
                              secondary_goals=TYPE_2_GOALS)

    base_page.scroll_to_bottom()
    base_element.send_user_input(input_data='04',
                                 input_field=CSS_SELECTORS["month_input"],
                                 wait_element=CSS_SELECTORS['footer_next'])
    base_element.send_user_input(input_data='11',
                                 input_field=CSS_SELECTORS["day_input"],
                                 wait_element=CSS_SELECTORS['footer_next'])
    base_element.send_user_input(input_data='1949',
                                 input_field=CSS_SELECTORS["year_input"],
                                 wait_element=CSS_SELECTORS['footer_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                              wait_element=CSS_SELECTORS['take_a_survey'])
