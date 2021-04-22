import requests
from pages import base_page
import re
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locators import CSS_SELECTORS


class SMSUtils:
    def __init__(self, browser):
        self.browser = browser
        self.base_element = BaseElement(browser)
        self.base_page = BasePage(browser)

    # this method returns the message based on an index from the list of responses
    @staticmethod
    def get_message_text(request_url='https://twilio-incoming-sms.herokuapp.com/message_history', index=int):
        try:
            response = requests.get(request_url).json()
            _, v = response[index].popitem()
            print('\033[92m Message received is: "{}" \033[0m'.format(v))
            return v
        except:
            base_page.print_error(message='\033[91m Message was not found \033[0m')

    # this method returns the url from a string
    @staticmethod
    def get_url_from_message(message):

        regex = "(?P<url>https?://[^\s]+)"

        try:
            print('\033[92m URL found is: "{}" \033[0m'.format(re.search(regex, message).group("url")))

            return re.search(regex, message).group("url")
        except:
            base_page.print_error(message='\033[91m URL was not found \033[0m')

    # this method decodes a short url
    @staticmethod
    def decode_url(url):
        try:
            long_url = urllib.request.urlopen(url)
            print('\033[92m Decoded URL is: "{}" \033[0m'.format(long_url.geturl()))
            return long_url.geturl()
        except:
            base_page.print_error(message='\033[91m URL could not be decoded \033[0m')

    # this method return the token from the url
    @staticmethod
    def get_token_from_url(long_url):
        try:
            token = long_url.split("?")
            print('\033[92m Token is: "{}" \033[0m'.format(token[-1]))
            return token[-1]
        except:
            base_page.print_error(message='\033[91m Token could not be retrieved \033[0m')

    def sms_tool_url_loader(self, phone_number):
        self.base_page.load_url(subdomain='twilio-incoming-sms.',
                                top_level_domain='message_list?', second_level_domain='herokuapp.com/',
                                subdirectory='from_number=1', path=phone_number,
                                wait_element=CSS_SELECTORS["sms_tool_header"])

    def sms_reply(self, reply):
        try:
            user_input = self.browser.find_element_by_id("sms_reply_1")
            user_input.click()
            user_input.clear()
            user_input.send_keys(reply)
        except:
            print('\033[91mUser input could not be sent\033[0m')

        self.browser.find_element_by_id("sms_reply_1").send_keys(Keys.RETURN)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable, "h2[class='heading-section']")
