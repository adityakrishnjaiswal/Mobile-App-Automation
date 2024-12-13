# browserstack_status.py
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv(r"C:\Users\Admin\Desktop\Automation-Projects\Mobile-App-Automation\resources\.env")

def update_log(session_id, status):
    """
    Function to update the session status on BrowserStack.

    :param session_id: The session ID of the BrowserStack test session.
    :param status: The status of the test ('passed' or 'failed').
    """
    username = os.getenv("BS_USER")
    access_key = os.getenv("BS_KEY")

    url = f'https://api.browserstack.com/automate/sessions/{session_id}.json'
    data = {'status': status}
    
    # Make an API request to update session status
    response = requests.put(url, auth=(username, access_key), data=json.dumps(data))

    if response.status_code == 200:
        print(f'Session {session_id} marked as {status} on BrowserStack.')
    else:
        print(f'Failed to update BrowserStack session status. Response: {response.text}')
