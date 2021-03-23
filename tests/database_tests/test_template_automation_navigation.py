# this is a test template
from pages.base_page import BasePage
from pages.base_element import BaseElement
from pages.locators import CSS_SELECTORS, CSS_SELECTORS_LIFEMAP_CARDS
from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS
from pymongo import MongoClient


# ****** Test Title *****

def test_template(browser):
    # 1. Go to the starting link and arrive at the landing page.

    base_page = BasePage(browser)
    base_element = BaseElement(browser)
    base_page.load_url(subdomain='tinyurl.com/y2kco4t9',
                       top_level_domain='', second_level_domain='', subdirectory='',
                       path='', wait_element='div[id="app"]')
    base_element.button_click(button_selector=CSS_SELECTORS['start_my_profile'],
                              wait_element=CSS_SELECTORS['header_back'])

    base_element.button_click(button_selector=CSS_SELECTORS['header_back'],
                              wait_element=CSS_SELECTORS['start_my_profile'])
    base_element.button_click(button_selector=CSS_SELECTORS['start_my_profile'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS['footer_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS['footer_next'])

    base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS['footer_next'])

    base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_4'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_5'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                              wait_element=CSS_SELECTORS['footer_next'])

    base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                              wait_element=CSS_SELECTORS['footer_next'])

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





