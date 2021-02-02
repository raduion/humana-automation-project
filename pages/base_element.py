from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BaseElement:

    def __init__(self, browser):
        self.browser = browser

    # this is a method that asserts if a text is present in the page

    def check_text_displayed(self, text, css_element):

        text_displayed = self.browser.find_element_by_css_selector(css_element)

        try:
            assert text in text_displayed.text
            print('The text displayed is: "{}"'.format(text))
        except:
            print_error(message="There is a different text displayed: {}".format(text_displayed.text))
            raise

    # this method clicks on a button in the page

    def button_click(self, button_selector='css_selector', wait_element='css_wait_selector'):
        try:
            button = self.browser.find_element_by_css_selector(button_selector)
            button.click()
            print('\033[92m Button was successfully clicked: "{}"\033[0m'.format(wait_element))
        except:
            print_error(message='Button could not be clicked: "{}"'.format(wait_element))

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located, wait_element)

    # this method chooses a selection from a drop down using Select

    def select_option_from_dropdown(self, select_option='css_selector', wait_element='css_wait_selector', index=1):

        try:
            dropdown_options = self.browser.find_elements_by_css_selector(select_option)
            for x in range(0, len(dropdown_options)):
                if dropdown_options[x].is_displayed():
                    dropdown_options[x] = Select(dropdown_options[x])
                    dropdown_options[x].select_by_index(index)
                    selected_answer = dropdown_options[x].first_selected_option
                    print('\033[92m Option was selected: "{}"\033[0m'.format(selected_answer.text))
        except:
            print_error(message='"{}" option could not be selected'.format(selected_answer.text))

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable, wait_element)

    # this method selects an option from a list

    def select_option_from_list(self, option_selector='css_option_selector', selected_option_selector='css_selector',
                                wait_element='css_wait_selector', index=-1):

        try:
            self.browser.find_element_by_css_selector(option_selector).click()
            selected_option = self.browser.find_elements_by_css_selector(selected_option_selector)[index]
            print('\033[92m List answer was selected: "{}"\033[0m'.format(selected_option.text))
            return selected_option.text
        except:
            print_error(message='List answer could not be selected: "{}"'.format(selected_option.text))

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable, wait_element)

    # this method selects radio options

    def select_options_from_radio(self, radio_selector='css_selector', wait_element='css_wait_selector'):
        count = len(self.browser.find_elements_by_css_selector(radio_selector))
        try:
            for x in range(0, count):
                radio_option = self.browser.find_elements_by_css_selector(radio_selector)[x]
                if radio_option.is_displayed():
                    radio_option.click()
                    print('\033[92m All available radio options were selected. \033[0m')
        except:
            print_error(message='Radio options could not be selected.')

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable, wait_element)

    # this method sends a date of birth

    def send_dob(self, month_index, day_index, year_index, month_selector='css_month_selector',
                 day_selector='css_day_selector', year_selector='css_year_selector', wait_element='css_wait_selector'):

        try:
            month_selector = Select(self.browser.find_element_by_css_selector(month_selector))
            month_selector.select_by_index(month_index)
            print('The selected DOB month is {}'.format(month_index))
        except:
            print_error(message='The DOB month could not be selected')

        try:
            day_selector = Select(self.browser.find_element_by_css_selector(day_selector))
            day_selector.select_by_index(day_index)
            print('The selected DOB day is {}'.format(day_index))
        except:
            print_error(message='The DOB day could not be selected')

        try:
            year_selector = Select(self.browser.find_element_by_css_selector(year_selector))
            year_selector.select_by_index(year_index)
            print('The selected DOB year is {}'.format(2002 - (year_index - 1)))
        except:
            print_error(message='The DOB year could not be selected')

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable, wait_element)

    # this method sends a value for input fields requiring user input

    def send_user_input(self, input_data, input_field='css_selector', wait_element='css_wait_selector'):

        try:
            user_input = self.browser.find_element_by_css_selector(input_field)
            user_input.click()
            user_input.clear()
            user_input.send_keys(input_data)
            print('The user input sent is: {}'.format(input_data))
        except:
            print_error(message='User input could not be sent')

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable, wait_element)

    # this is a method that checks all the available checkboxes

    def checkbox_selection(self, checkbox_selector='css_selector', wait_element='css_wait_selector'):

        try:
            checkbox = self.browser.find_elements_by_css_selector(checkbox_selector)
            for x in range(0, len(checkbox)):
                if checkbox[x].is_displayed():
                    checkbox[x].click()
            print('All checkboxes were selected')
        except:
            print_error(message='Checkboxes could not be selected')

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable, wait_element)


# this is a method that prints an error and also raise an exception to stop the execution of the test

def print_error(message):
    print('\033[91m {} \033[0m'.format(message))
    raise
