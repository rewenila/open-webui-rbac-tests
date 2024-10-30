import requests


def get_user_by_id(auth_token, user_id, base_url):
    response = requests.get(f'{base_url}/api/v1/users/{user_id}',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response


def delete_user_by_id(auth_token, user_id, base_url):
    response = requests.delete(f'{base_url}/api/v1/users/{user_id}',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response


def change_user_role(auth_token, user_id, base_url):
    response = requests.post(f'{base_url}/api/v1/users/update/role',
                            json={
                                "id": user_id,
                                "role": "user"
                            },
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response


