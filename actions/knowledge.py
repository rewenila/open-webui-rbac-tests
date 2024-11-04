import requests


def get_all_knowledge(auth_token, base_url):
    response = requests.get(f'{base_url}/api/v1/knowledge/',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response
    

def create_knowledge(auth_token, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/knowledge/create', json=payload,
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response


def update_knowledge_by_id(auth_token, knowledge_id, payload, base_url):
    response = requests.post(f'{base_url}/api/v1/knowledge/{knowledge_id}/update', json=payload,
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response


def delete_knowledge_by_id(auth_token, knowledge_id, base_url):
    response = requests.delete(f'{base_url}/api/v1/knowledge/{knowledge_id}/delete',
                            headers={
                                "Content-Type": "application/json",
                                "authorization": f'Bearer {auth_token}'
                            },
                            verify=False)
    return response
