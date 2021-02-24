# this is a test template
from pages.base_page import BasePage
import os
from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS
from pymongo import MongoClient
import json
import time
import requests
from pages.gmail.email_operations import EmailOperations

from pages.sms_handler import SMSHandlers


# ****** Test Title *****

def test_template(browser):
    # 1. Go to the starting link and arrive at the landing page.

    base = BasePage(browser)
    sms = SMSHandlers()
    email = EmailOperations()
    db = Connect()

    base.load_url(subdomain='twilio-incoming-sms.', second_level_domain='herokuapp.',
                  subdirectory='/message_history', path='',
                  wait_element='div[id="json"]')
    # string = sms.get_message_text(index=-2)
    # url = sms.get_url_from_message(string)
    # base.load_url(scheme=url,
    #               subdomain='',
    #               top_level_domain='',
    #               second_level_domain='',
    #               subdirectory='',
    #               path='',
    #               wait_element='div[id="app"]')
    # long_url = sms.decode_url(url=url)
    # sms.get_token_from_url(long_url=long_url)

    url = email.get_email_url()
