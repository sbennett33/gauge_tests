import os

import requests
from getgauge.python import step, data_store

@step("Create a client in the <name> namespace")
def create_a_client_in_the_namespace(name):
    headers = {'Authorization': 'Bearer ' + data_store.scenario.token, 'Content-Type': 'application/vnd.api+json'}
    json = {
        'data': {
            'type': 'clients',
        }
    }
    r = requests.post(f'{os.getenv("API_BASE_URL")}/namespaces/{name}/clients',
                      headers=headers, json=json)
    assert r.status_code == 201
    data_store.scenario.client = r.json()

@step("Ensure the client exists")
def ensure_the_client_exists():
    assert False, "Add implementation code"

@step("Ensure the client has permission to manage <resource> in the <namespace> namespace")
def ensure_the_client_has_permission_to_manage_in_the_current_namespace(resource, namespace):
    assert False, "Add implementation code"
