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


def update_user_payload():
    payload = {
        "name": "Updated John Doe",
        "email": "updated.john.doe@test.com",
        "profile_image_url": "/user.png",
        "password": "test456",
    }

    return payload


def create_empty_chat_payload():
    payload = {
        "chat": {}
    }
    
    return payload


def update_admin_config_payload(
    should_show_admin_details: bool,
    should_enable_signup: bool,
    default_user_role: str,
    should_enable_community_sharing: bool,
    should_enable_message_rating: bool,
) -> dict:
    payload = {
        "SHOW_ADMIN_DETAILS": should_show_admin_details,
        "ENABLE_SIGNUP": should_enable_signup,
        "DEFAULT_USER_ROLE": default_user_role,
        "JWT_EXPIRES_IN": "-1",
        "ENABLE_COMMUNITY_SHARING": should_enable_community_sharing,
        "ENABLE_MESSAGE_RATING": should_enable_message_rating,
    }

    return payload

