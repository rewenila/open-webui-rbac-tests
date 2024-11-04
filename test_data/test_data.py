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


def add_second_user_payload(role=None):
    payload = {
        "name": "Jane Doe",
        "email": "jane.doe@test.com",
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


def update_password_payload():
    payload = {"password": "test123", "new_password": "test456"}

    return payload


def update_profile_payload():
    payload = {"profile_image_url": "/updated_user.png", "name": "Updated John Doe"}

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


def add_model_payload():
    payload = {
        "id": "test_model",
        "base_model_id": "gemma:2b",
        "name": "Test Model",
        "meta": {
            "profile_image_url": "/model.png",
            "description": "Test model based on gemma:2b",
            "capabilities": {"vision": True},
            "additionalProp1": {},
        },
        "params": {"additionalProp1": {}},
    }

    return payload


def update_model_payload():
    payload = {
        "id": "test_model",
        "base_model_id": "gemma:2b",
        "name": "Updated Test Model",
        "meta": {
            "profile_image_url": "/updated_model.png",
            "description": "Updated test model based on gemma:2b",
            "capabilities": {"vision": False},
            "additionalProp1": {},
        },
        "params": {"additionalProp1": {}},
    }

    return payload


def update_user_settings_payload():
    payload = {
        "ui": {
            "landingPageMode": "chat",
            "chatBubble": True,
            "notificationEnabled": True,
            "showUsername": True,
            "widescreenMode": True,
            "chatDirection": "RTL",
            "splitLargeChunks": False,
            "scrollOnBranchChange": True,
            "speechAutoSend": False,
        },
        "additionalProp1": {},
    }

    return payload


def create_prompt_payload():
    payload = {
        "command": "/test-prompt",
        "title": "Test Prompt",
        "content": "This is a test prompt.",
    }

    return payload


def update_prompt_payload():
    payload = {
        "command": "/test-prompt",
        "title": "Updated Test Prompt",
        "content": "This is the updated test prompt.",
    }

    return payload


def create_knowledge_payload():
    payload = {
        "name": "Test Knowledge",
        "description": "This is a test knowledge base",
        "data": {},
    }

    return payload


def update_knowledge_payload():
    payload = {
        "name": "Updated Test Knowledge",
        "description": "This is the updated test knowledge base",
        "data": {},
    }

    return payload

