import requests


def get_all_prompts(auth_token, base_url):
    response = requests.get(f'{base_url}/api/v1/prompts/',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response
    

def create_prompt(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/prompts/create', json=payload,
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response


def update_prompt_by_command(auth_token, command, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/prompts/command{command}/update', json=payload,
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response


def delete_prompt_by_command(auth_token, command, base_url):
    response = requests.delete(f'{base_url}/api/v1/prompts/command{command}/delete',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response
