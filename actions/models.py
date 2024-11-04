import requests


def get_all_models(auth_token, base_url):
    response = requests.get(f'{base_url}/api/v1/models/',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response
    

def add_model(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/models/add', json=payload,
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response


def update_model_by_id(auth_token, model_id, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/models/update', json=payload,
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            params={
                                "id": model_id
                            },
                            verify=False)
    return response


def delete_model_by_id(auth_token, model_id, base_url):
    response = requests.delete(f'{base_url}/api/v1/models/delete',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            params={
                                "id": model_id
                            },
                            verify=False)
    return response
