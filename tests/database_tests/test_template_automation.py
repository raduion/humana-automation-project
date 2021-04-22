# this is a test template
from pages.base_page import BasePage
from pages.base_element import BaseElement
import requests


# ****** Test Title *****

def test_template(browser):
    # 1. Go to the starting link and arrive at the landing page.

    base_page = BasePage(browser)
    base_element = BaseElement(browser)

    # base_page.load_url(subdomain='tinyurl.com/ya8pvsb3',
    #                    top_level_domain='', second_level_domain='', subdirectory='',
    #                    path='', wait_element='div[id="app"]')
    # base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
    #                           wait_element=CSS_SELECTORS['footer_next'])
    # base_element.send_user_input(input_data='ceva acolo',
    #                              input_field=CSS_SELECTORS['text_input'],
    #                              wait_element=CSS_SELECTORS['footer_next'])
    # base_element.select_option_from_radio(radio_selector=CSS_SELECTORS['radio_option'],
    #                                       option_number=0,
    #                                       wait_element=CSS_SELECTORS['footer_next'])
    # base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
    #                           wait_element=CSS_SELECTORS['footer_next'])
    # base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
    #                           wait_element=CSS_SELECTORS['footer_next'])

    url = 'https://twilio-incoming-sms.herokuapp.com/message_list'
    value = 'START'

    requests.post(url, data=value)

    # test

