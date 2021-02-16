# this is a test template
from pages.base_page import BasePage
from pages.base_element import BaseElement
from pages.css_selectors import CSS_SELECTORS_LIFEMAP, CSS_SELECTORS_LIFEMAP_CARDS
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
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['start_my_profile'],
                              wait_element=CSS_SELECTORS_LIFEMAP['header_back'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['header_back'],
                              wait_element=CSS_SELECTORS_LIFEMAP['start_my_profile'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['start_my_profile'],
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
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
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
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_next'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_next'],
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
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
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
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_next'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_next'],
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
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'],
                              wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_3'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_cards_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_cards_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_next'])

    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP['footer_next'])

    base_page.scroll_to_bottom()
    base_element.send_user_input(input_data='04',
                                 input_field=CSS_SELECTORS_LIFEMAP["month_input"],
                                 wait_element=CSS_SELECTORS_LIFEMAP['footer_next'])
    base_element.send_user_input(input_data='11',
                                 input_field=CSS_SELECTORS_LIFEMAP["day_input"],
                                 wait_element=CSS_SELECTORS_LIFEMAP['footer_next'])
    base_element.send_user_input(input_data='1949',
                                 input_field=CSS_SELECTORS_LIFEMAP["year_input"],
                                 wait_element=CSS_SELECTORS_LIFEMAP['footer_next'])
    base_element.button_click(button_selector=CSS_SELECTORS_LIFEMAP['footer_next'],
                              wait_element=CSS_SELECTORS_LIFEMAP['take_a_survey'])




