from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locators import CSS_SELECTORS, WELLNESS_CATEGORIES_CSS_SELECTORS_0002, WELLNESS_CATEGORIES_CSS_SELECTORS_0006
from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS, DATABASE_KEYS
import time

WELLNESS_ANSWERS_0002 = {
    'Answer 1': WELLNESS_CATEGORIES_CSS_SELECTORS_0002['Mental Health'],
    'Answer 2': WELLNESS_CATEGORIES_CSS_SELECTORS_0002['Healthy eating'],
    'Answer 3': WELLNESS_CATEGORIES_CSS_SELECTORS_0002['Social well-being'],
    'Answer 4': WELLNESS_CATEGORIES_CSS_SELECTORS_0002['Exercise'],
    'Answer 5': WELLNESS_CATEGORIES_CSS_SELECTORS_0002['Putting my talents to work'],
    'Answer 6': WELLNESS_CATEGORIES_CSS_SELECTORS_0002['I don"t have a goal yet'],
    'Answer 7': WELLNESS_CATEGORIES_CSS_SELECTORS_0002['None of these']
}

WELLNESS_ANSWERS_0006 = {
    'Answer 1': WELLNESS_CATEGORIES_CSS_SELECTORS_0006['Not enough time'],
    'Answer 2': WELLNESS_CATEGORIES_CSS_SELECTORS_0006['Lack of support'],
    'Answer 3': WELLNESS_CATEGORIES_CSS_SELECTORS_0006['Can’t find the energy'],
    'Answer 4': WELLNESS_CATEGORIES_CSS_SELECTORS_0006['I’m not confident I can do it'],
    'Answer 5': WELLNESS_CATEGORIES_CSS_SELECTORS_0006['Need more information'],
    'Answer 6': WELLNESS_CATEGORIES_CSS_SELECTORS_0006['Cost is too much'],
    'Answer 7': WELLNESS_CATEGORIES_CSS_SELECTORS_0006['My barrier is not on this list'],
    'Answer 8': WELLNESS_CATEGORIES_CSS_SELECTORS_0006['I don’t have any barriers right now']
}


class WellnessUtils:

    def __init__(self, browser):
        self.browser = browser
        self.base_element = BaseElement(browser)
        self.base_page = BasePage(browser)
        self.connect = Connect()

    # this method loads a Wellness URL

    def wellness_url_loader(self, memberpersonalgeneratedkey, track_id_value):

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
            if x['trackId'] == track_id_value:
                i = i + 1
                tiny_url = x['url']
                self.base_page.load_url(scheme='',
                                        subdomain=tiny_url,
                                        top_level_domain='',
                                        second_level_domain='',
                                        subdirectory='',
                                        path='',
                                        wait_element=CSS_SELECTORS["footer_next"])
                time.sleep(1)

        if i == 0:
            print('\033[91m Tiny URL was not found. \033[0m')
            raise

    # this method passes a Wellness intro

    def wellness_intro_passer(self):
        self.base_page.scroll_to_bottom()

        time.sleep(2)

        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])

    # this method passes a Wellness activity

    def wellness_activity_passer_0002(self, wellness_activity_answer):

        print('User started Wellness activity on 0002')

        self.base_element.send_user_input(input_data='This is an automated answer for the first question',
                                          input_field=CSS_SELECTORS["text_input"],
                                          wait_element=CSS_SELECTORS['footer_next'])
        if wellness_activity_answer in [WELLNESS_ANSWERS_0002['Answer 3'], WELLNESS_ANSWERS_0002['Answer 4'],
                                        WELLNESS_ANSWERS_0002['Answer 5'], WELLNESS_ANSWERS_0002['Answer 6'],
                                        WELLNESS_ANSWERS_0002['Answer 7']]:
            self.base_page.scroll_to_bottom()
            time.sleep(2)
        self.base_element.button_click(button_selector=wellness_activity_answer,
                                       wait_element=CSS_SELECTORS['footer_next'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])
        time.sleep(2)

    def wellness_activity_passer_0006(self, wellness_activity_answer):

        print('User started Wellness activity on 0006')

        if wellness_activity_answer in [WELLNESS_ANSWERS_0006['Answer 3'], WELLNESS_ANSWERS_0006['Answer 4'],
                                        WELLNESS_ANSWERS_0006['Answer 5'], WELLNESS_ANSWERS_0006['Answer 6'],
                                        WELLNESS_ANSWERS_0006['Answer 7'], WELLNESS_ANSWERS_0006['Answer 8']]:
            self.base_page.scroll_to_bottom()
            time.sleep(2)
        self.base_element.button_click(button_selector=wellness_activity_answer,
                                       wait_element=CSS_SELECTORS['footer_next'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])
        time.sleep(2)
