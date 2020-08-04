import os
from datetime import datetime

import requests
from getgauge.python import data_store, step


@step("Call <endpoint> endpoint")
def assert_get_endpoint(endpoint):
    headers = {'Authorization': 'Bearer ' + data_store.scenario.token}
    r = requests.get(f'{os.getenv("API_BASE_URL")}{endpoint}', headers=headers)
    assert r.status_code == 200
    assert len(r.json()) > 0


@step("Create a test namespace")
def create_a_test_namespace():
    test_namespace = "test-namespace-" + \
        str(datetime.timestamp(datetime.now()))
    headers = {'Authorization': 'Bearer ' + data_store.scenario.token,
               'Content-Type': 'application/vnd.api+json'}
    json = {
        'data': {
            'type': 'namespaces',
            'id': test_namespace,
            'attributes': {
                'metadata': {}
            }
        }
    }
    r = requests.post(f'{os.getenv("API_BASE_URL")}/namespaces',
                      headers=headers, json=json)
    assert r.status_code == 201
    data_store.scenario.test_namespace = test_namespace


@step("Delete test namespace")
def delete_test_namespace():
    assert False, "Add implementation code"


@step("Create <name> namespace")
def create_namespace(name):
    headers = {'Authorization': 'Bearer ' + data_store.scenario.token,
               'Content-Type': 'application/vnd.api+json'}
    json = {
        'data': {
            'type': 'namespaces',
            'id': name,
            'attributes': {
                'metadata': {}
            }
        }
    }
    r = requests.post(f'{os.getenv("API_BASE_URL")}/namespaces',
                      headers=headers, json=json)
    assert r.status_code == 201
    data_store.scenario.test_namespace = name
