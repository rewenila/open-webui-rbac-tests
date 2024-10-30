import requests


def do_login(email, password, base_url):
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(f'{base_url}/api/v1/auths/signin', json=payload,
                             headers={"Content-Type": "application/json"},
                             verify=False)

    return response


def signup_user(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/auths/signup', json=payload,
                             headers={
                                 "Content-Type": "application/json",
                                 "authorization": f'Bearer {auth_token}'
                             },
                             verify=False)

    return response


def get_admin_config(auth_token, base_url):
    response = requests.get(f'{base_url}/api/v1/auths/admin/config',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)

    return response

