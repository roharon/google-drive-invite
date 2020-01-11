import requests
from flask import request
import json
import os

"""
need to set environment variable

'authorization_code'
'client_id'
'client_secret'
"""

def get_token():
    redirect_uri = request.host + "/code"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    REFRESH_TOKEN_URL = "www.googleapis.com/oauth2/v4/token?" \
        + "code=" + os.environ['authorization_code'] + "&client_id=" + os.environ['client_id'] \
            + "&client_secret=" + os.environ['client_secret'] \
            + "&redirect_uri=" + redirect_uri + "&grant_type=authorization_code"

    result = requests.post(REFRESH_TOKEN_URL, headers=headers)

    if(result.status_code == 200):
        result_json = result.json()
        return result_json['access_token']
    else:
        return "500"


def share_task(email_address=None):

    file_id = os.environ('file_id')
    PERMISSION_URL = "https://www.googleapis.com/drive/v3/files/" + file_id + "/permissions"

    token = get_token()

    if token == "500":
        return "ERROR"
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }

    data = {
        "role": "writer",
        "type": "user",
        "emailAddress": email_address
    }

    data = json.dumps(data)
    res = requests.post(PERMISSION_URL, headers=header, data=data)
    
    return res.json()