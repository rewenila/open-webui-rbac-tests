import requests


def create_chat(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/chats/new', json=payload,
                             headers={
                                 "Content-Type": "application/json",
                                 "authorization": f'Bearer {auth_token}'
                             },
                             verify=False)

    return response


def get_chat_list_by_session_user(auth_token, base_url):
    response = requests.get(f'{base_url}/api/v1/chats/list',
                             headers={
                                 "Content-Type": "application/json",
                                 "authorization": f'Bearer {auth_token}'
                             },
                            verify=False)
    return response


def get_chat_list_by_user_id(auth_token, user_id, base_url):
    response = requests.get(f'{base_url}/api/v1/chats/list/user/{user_id}',
                             headers={
                                 "Content-Type": "application/json",
                                 "authorization": f'Bearer {auth_token}'
                             },
                            verify=False)
    return response

