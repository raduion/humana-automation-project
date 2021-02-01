# this is a test template
from pages.base_class import BaseClass


# ****** Test Title *****

def test_template(browser):
    # 1. Go to the starting link and arrive at the landing page.

    base = BaseClass(browser)
    base.load_url(subdomain='google.', second_level_domain='', subdirectory='', path='',
                  wait_element='input[type="text"]')

    test_email = base.generate_unique_email(user='radu.ion')