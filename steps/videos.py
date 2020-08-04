from datetime import datetime, timezone
import os

import requests
from getgauge.python import data_store, step


@step("Create a video resource in the <namespace> namespace")
def create_a_video_resource_in_the_namespace(namespace):
    headers = {'Authorization': 'Bearer ' + data_store.scenario.token,
               'Content-Type': 'application/vnd.api+json'}

    json = {
        'data': {
            'type': 'videos',
            'attributes': {
                'startedAt': datetime.now(timezone.utc).isoformat()
            }
        }
    }

    r = requests.post(f'{os.getenv("API_BASE_URL")}/namespaces/{namespace}/videos',
                      headers=headers, json=json)

    assert r.status_code == 201
    data_store.scenario.video = r.json()

@step("Delete video resource from the <namespace> namespace")
def delete_video_resource(namespace):
    headers = {'Authorization': 'Bearer ' + data_store.scenario.token,
               'Content-Type': 'application/vnd.api+json'}
    
    video_id = data_store.scenario.video['data']['id']

    r = requests.delete(f'{os.getenv("API_BASE_URL")}/namespaces/{namespace}/videos/{video_id}',
                      headers=headers)

    assert r.status_code == 200
