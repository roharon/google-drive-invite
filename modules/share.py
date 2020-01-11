import requests
from flask import request
import json
import os

"""
need to set environment variable

# on get_token Funtion

'client_id' : string
'client_secret' : string
'refresh_token' : string

----
# on share_task Function

'file_id' : string
'send_notification' : boolean
'email_message' : string
'role' : string - "owner", "organizer", "fileOrganizer", "writer", "commenter", "reader"

'verify_code': string
"""

def get_token():

    redirect_uri = request.host + "/code"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    REFRESH_TOKEN_URL = "https://www.googleapis.com/oauth2/v4/token?" \
            + "client_id=" + os.environ['client_id'] \
            + "&client_secret=" + os.environ['client_secret'] \
            + "&refresh_token=" + os.environ['refresh_token'] \
            + "&grant_type=refresh_token"


    result = requests.post(REFRESH_TOKEN_URL, headers=headers)

    if(result.status_code == 200):
        result_json = result.json()
        return result_json['access_token']

    else:
        return "500"


def share_task(email_address=None, verify_code=None):

    try:
        if verify_code != os.environ['verify_code']:
            return "400"
    except KeyError:
        return "500"

    file_id = os.environ['file_id']

    PERMISSION_URL = "https://www.googleapis.com/drive/v3/files/" + file_id + "/permissions?" \
        + "&sendNotificationEmail=" + os.environ['send_notification'] \
        + "&emailMessage=" + os.environ['email_message']

    token = get_token()

    if token == "500":
        return "500"
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }

    data = {
        "role": os.environ['role']
        "type": "user",
        "emailAddress": email_address
    }

    data = json.dumps(data)
    res = requests.post(PERMISSION_URL, headers=header, data=data)

    if res.status_code != 200:
        return "400"

    return res.json()