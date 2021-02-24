from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import re
import base64
import email
import urllib
import urllib.request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is created automatically when
    # the authorization flow completes for the first time.

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # get inbox messages
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No tokens found.')
    else:
        # get list of URLs from last received email
        for message in messages[:1]:

            message = service.users().messages().get(userId='me', id=message['id'], format='raw').execute()
            msg_str = base64.urlsafe_b64decode(message['raw'])
            mime_msg = email.message_from_bytes(msg_str)
            messageMainType = mime_msg.get_content_maintype()
            if messageMainType == 'text':
                message = mime_msg.get_payload()
                message = re.sub(r"\r\n", '', message)
                url_list = re.findall(r'(https?://\S+)', message, re.MULTILINE)
            else:
                print('Email does not contains text')

            # work some formatting magic to extract the Humana URL from the email HTML
            # these rules are hardcoded, might need improvements if email template changes
            matching = [s for s in url_list if "click?upn=3DMJ2" in s]
            sendgrid_url = re.sub(r"=", '', matching[0])
            sendgrid_url = re.sub(r'"', '', sendgrid_url)
            sendgrid_url = re.sub(r'(upn3D)', r'upn=', sendgrid_url)
            humana_url = urllib.request.urlopen(sendgrid_url)

            print(humana_url.geturl())
            return str(humana_url.geturl())


if __name__ == '__main__':
    main()
