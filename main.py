import os

import requests

public_forward_url = os.environ.get('PUBLIC_FORWARD_URL')
private_forward_url = os.environ.get('PRIVATE_FORWARD_URL')


def github_hook(request):
    body = request.get_json()

    github_headers = {
        header: value
        for header, value in request.headers.items()
        if header.lower().startswith('x-github')
    }

    if private_forward_url and body['repository']['private'] is False:
        requests.post(public_forward_url, json=body, headers=github_headers)

    if public_forward_url:
        requests.post(private_forward_url, json=body, headers=github_headers)

    return 'OK'
