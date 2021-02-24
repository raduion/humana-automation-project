import os
import subprocess

EMAIL_OPERATIONS_VARIABLES = {
    'gmail_dir': '/Users/radu/Documents/AutomationTemplate/Humana/humana-automation-project/pages/gmail',
    'path': '/Users/radu/anaconda3/envs/CondaEnvironment/bin/python',
    'script': '/Users/radu/Documents/AutomationTemplate/Humana/humana-automation-project/pages/gmail/return_email_url'
              '.py '

}


class EmailOperations:

    # this method returns the URLfound in the last received email on the Automation account
    # account used: humanaautomation@gmail.com/ Sfappworks1
    @staticmethod
    def get_email_url():
        os.chdir(EMAIL_OPERATIONS_VARIABLES['gmail_dir'])
        try:
            cmd = "{} {}".format(EMAIL_OPERATIONS_VARIABLES['path'], EMAIL_OPERATIONS_VARIABLES['script'])
            email_url = os.popen(cmd).read()
            print('\033[92m Humana URL was found: "{}" \033[0m'.format(email_url))

            return email_url

        except AttributeError:
            print('\033[91m No URL was found \033[0m')

    # this method extracts the Humana autologin token from a given url
    @staticmethod
    def get_token_from_url(url):
        try:
            token = url.split("welcome?", 1)[1]
            print('\033[92m Humana token was found: "{}" \033[0m'.format(token))

            return token

        except AttributeError:
            # welcome? not found in the original string
            print('\033[91m No token was found \033[0m')

    # this method compares two given tokens
    @staticmethod
    def compare_email_db_tokens(email_token, db_token):

        if email_token == db_token:

            print('\033[92m Email token ({}) matches DB token ({}). \033[0m'.format(email_token, db_token))
        else:
            print('\033[91m Email token ({}) does not match DB token ({}). \033[0m'.format(email_token, db_token))
