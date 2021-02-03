# this is a test template
from pages.base_page import BasePage
from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS
from pymongo import MongoClient


# ****** Test Title *****

def test_template(browser):
    # 1. Go to the starting link and arrive at the landing page.

    # base = BasePage(browser)
    # base.load_url(subdomain='google.', second_level_domain='', subdirectory='', path='',
    #               wait_element='input[type="text"]')

    Connect.return_documents(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                             db_name='stars-gl-core-dev',
                             collection_name='users')
    Connect.get_database_names(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'])
    Connect.get_collection_names(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                                 db_name='stars-gl-core-dev')
    Connect.return_document(connection_string=DATABASE_CONNECTION_STRINGS['phi_db'],
                            db_name='stars-gl-core-dev',
                            collection_name='users',
                            record={'memberPersonalGeneratedKey': '2975043039904'})
