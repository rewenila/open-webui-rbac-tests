import os

import pytest
from dotenv import load_dotenv

from actions.auths import do_login, add_user
from actions.chats import create_chat, get_chat_list_by_session_user
from actions.users import delete_user_by_id, change_user_role
from test_data.test_data import add_user_payload, create_empty_chat_payload


load_dotenv()


@pytest.fixture()
def setup_data(get_base_url):
    base_url = get_base_url
    
    admin_login_response = do_login(os.getenv('EMAIL'), os.getenv('PASSWORD'), base_url)
    admin_auth_token = admin_login_response.json()['token']

    add_pending_user_response = add_user(admin_auth_token, add_user_payload("pending"), base_url)
    assert add_pending_user_response.status_code == 200, f"[ERROR] {add_pending_user_response.json()['detail']}"
    assert add_pending_user_response.json()["id"] is not "", "[ERROR] ID is empty"
    assert add_pending_user_response.json()["token"] is not "", "[ERROR] Token is empty"
    assert add_pending_user_response.json()["role"] == "pending", "[ERROR] User created with incorrect role"

    user_auth_token = add_pending_user_response.json()["token"]
    user_id = add_pending_user_response.json()["id"] 
    
    yield admin_auth_token, user_auth_token, user_id, base_url

    delete_user_by_id(admin_auth_token, user_id, base_url)


def test_pending_user_can_login(setup_data):
    _, _, _, base_url = setup_data

    login_user_response = do_login(add_user_payload()["email"], add_user_payload()["password"], base_url)
    assert login_user_response.status_code == 200, '[ERROR] User could not log in'
    assert login_user_response.json()['token'] != "", '[ERROR] Bearer token came empty'


def test_pending_user_cannot_change_own_role(setup_data):
    _, user_auth_token, user_id, base_url = setup_data

    change_user_role_response = change_user_role(user_auth_token, user_id, base_url)
    assert change_user_role_response.status_code == 401, "[ERROR] Pending user was allowed to change its own role"


def test_pending_user_does_not_have_chat_permissions(setup_data):
    _, user_auth_token, _, base_url = setup_data

    create_chat_response = create_chat(user_auth_token, create_empty_chat_payload(), base_url)
    assert create_chat_response.status_code == 401, "[ERROR] Pending user was allowed to create chat"

    get_chats_response = get_chat_list_by_session_user(user_auth_token, base_url)
    assert get_chats_response.status_code == 401, "[ERROR] Pending user was allowed to access own chat list"

