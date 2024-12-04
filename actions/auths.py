import requests


def do_login(email, password, base_url):
    payload = {
        'email': email,
        'password': password
    }

    print(f"Trying to sign in to {base_url}/api/v1/auths/signin with credentials {payload}")

    response = requests.post(f'{base_url}/api/v1/auths/signin', json=payload,
                             headers={"Content-Type": "application/json"},
                             verify=False)

    return response


def signup_user(auth_token, payload, base_url):
    print(f"Trying to sign up to {base_url}/api/v1/auths/signup with credentials {payload}")

    response = requests.post(f'{base_url}/api/v1/auths/signup', json=payload,
                             headers={
                                 "Content-Type": "application/json",
                                 "authorization": f'Bearer {auth_token}'
                             },
                             verify=False)

    return response


def add_user(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/auths/add', json=payload,
                             headers={
                                 "Content-Type": "application/json",
                                 "authorization": f'Bearer {auth_token}'
                             },
                             verify=False)

    return response


def update_password(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/auths/update/password', json=payload,
                             headers={
                                 "Content-Type": "application/json",
                                 "authorization": f'Bearer {auth_token}'
                             },
                             verify=False)

    return response


def update_profile(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/auths/update/profile', json=payload,
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


def update_admin_config(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/auths/admin/config', json=payload,
                             headers={
                                 "Content-Type": "application/json",
                                 "authorization": f'Bearer {auth_token}'
                             },
                             verify=False)

    return response

