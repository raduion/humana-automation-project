from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from datetime import datetime


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    # this is a method that loads an URL
    #
    # e.g:  https://site.example.com/software/index.html

    def load_url(self, scheme='https://', subdomain='site.', second_level_domain='example.', top_level_domain='com',
                 subdirectory='/software', path='/index.html', wait_element='css_wait_selector'):
        try:

            default_wait_time_for_load_seconds = 30
            url_to_load = '{}{}{}{}{}{}'.format(scheme, subdomain, second_level_domain,
                                                top_level_domain, subdirectory, path)
            self.browser.get(url_to_load)

            WebDriverWait(self.browser, default_wait_time_for_load_seconds).until(
                EC.element_to_be_clickable, wait_element)

        except:
            print_error(message='\033[92mCould not reach {}{}{}{}{}{} URL. \033[0m'.
                        format(scheme, subdomain, second_level_domain, top_level_domain, subdirectory, path))

    # this is a method that returns the response of a network call and bypass the login for a service call by setting
    # a temporary login cookie

    def private_session_response(self, api_path, cookie_header=None, request_url='request_url'):

        # Note that a login cookie expires in ~2 weeks

        if cookie_header is None:
            cookie_header = {
                "Cookie": "sessionid=.eJxVjLEKwjAURf8ls7ZgLaKbcegkKC04htfk2YTapCZpFMR_NwGXjPcezvkQjW9PDqR8Qk"
                          "lWZDBmeODawOLlhjkPHiOs-mtFYdqGjp6bS-heop6R1u18uu-nm22iyJLBFoeWKZGUXX72wEfUiaRZJIDa"
                          "Kw5eGV20aIPiSMGhOGaI_r0sJsHJWCLfH09fQtQ:1kwNC1:3B9kZbnpFDCE0-KSeF9WkMpSVUE"}

        session = requests.Session()

        session.headers.update(cookie_header)

        requested_url = '{}{}'.format(request_url, api_path)

        response = session.get(requested_url, headers=session.headers)

        return response

    # this is a method that returns a network call recorded for a provided request URL

    def return_found_request(self, request_url='request_url', list_position=-1):

        try:

            request_list = []

            for request in self.browser.requests:
                if request.path == request_url:
                    request_list.append(request)

            return request_list[list_position]

        except:

            print_error(message='\033[91mThe required request was not found \033[0m')

    # this is a method that returns the value of a key from a mixed dictionary list

    @staticmethod
    def return_list_value(test_list, key):

        try:
            value = [val[key] for val in test_list if key in val][0]
            return value
        except:
            print_error(message='The requested "{}" key value could npt be returned'.format(key))

    @staticmethod
    def generate_unique_email(user='user_account'):

        unique_timestamp = datetime.timestamp(datetime.now())
        unique_generated_email = ('{}+{}@sfappworks.com'.format(user, int(unique_timestamp)))

        return unique_generated_email

    # this is a method that scrolls to the bottom of a page

    def scroll_to_bottom(self):
        try:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except:
            print_error(message="Page couldn't be scrolled")

    @staticmethod
    def get_timestamp():
        dateTimeObj = datetime.utcnow()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        print('Current Timestamp : ', timestampStr)


# this is a method that prints an error and also raise an exception to stop the execution of the test

def print_error(message):
    print('\033[91m{} \033[0m'.format(message))
    raise
