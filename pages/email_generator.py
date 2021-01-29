from datetime import datetime


class UniqueEmail:
    reusable_now = datetime.now()
    reusable_timestamp = datetime.timestamp(reusable_now)

    reusable_generated_email = ('radu.ion+', str(int(reusable_timestamp)), '@sfappworks.com')

    def __init__(self, browser):
        self.browser = browser

    def send_reusable_email(self, email_field_selector='css_email_selector'):
        email_field = self.browser.find_element_by_css_selector(email_field_selector)
        email_field.click()
        email_field.clear()

        email_field.send_keys(self.reusable_generated_email)

        print('User email is:', self.reusable_generated_email)

    def send_unique_email(self, email_field_selector='css_email_selector'):
        unique_now = datetime.now()
        unique_timestamp = datetime.timestamp(unique_now)

        unique_generated_email = ('radu.ion+{}@sfappworks.com'.format(int(unique_timestamp)))

        email_field = self.browser.find_element_by_css_selector(email_field_selector)
        email_field.click()
        email_field.clear()

        email_field.send_keys(unique_generated_email)

        print('User email is:', unique_generated_email)

        return unique_generated_email
