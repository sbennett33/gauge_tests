import os

import jwt
import requests
from getgauge.python import Messages, before_scenario, data_store, step


@step('Get an access token with <scope> scope')
def assert_access_token(scope):
    auth_base_url = os.getenv("AUTH_BASE_URL")
    auth_audience = os.getenv("AUTH_AUDIENCE")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    json = {
        'client_id': client_id,
        'client_secret': client_secret,
        'audience': auth_audience,
        'grant_type': 'client_credentials'
    }

    r = requests.post(f'{auth_base_url}/oauth/token', json=json)
    token = r.json()['access_token']
    claims = jwt.decode(token, verify=False)
    assert scope in claims['permissions']
    data_store.scenario.token = token
