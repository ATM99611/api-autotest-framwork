import requests


def mo3(**request_data):
    resp =requests.request(**request_data)
    return resp
