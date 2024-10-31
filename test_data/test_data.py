def signup_user_payload():
    payload = payload = {
        "name": "John Doe",
        "email": "john.doe@test.com",
        "password": "test123",
        "profile_image_url": "/user.png",
    }

    return payload


def add_user_payload(role=None):
    payload = {
        "name": "John Doe",
        "email": "john.doe@test.com",
        "password": "test123",
        "profile_image_url": "/user.png",
    }

    if role is not None:
        payload["role"] = role

    return payload


def create_empty_chat_payload():
    payload = {
        "chat": {}
    }
    
    return payload

