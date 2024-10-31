import os

import pytest
from dotenv import load_dotenv

from actions.auths import do_login, signup_user, add_user, update_admin_config
from actions.chats import get_chat_list_by_user_id
from actions.users import delete_user_by_id, get_all_users, change_user_role, update_user_by_id
from test_data.test_data import *


load_dotenv()


@pytest.fixture()
def setup_data(get_base_url):
    base_url = get_base_url

    response = do_login(os.getenv('EMAIL'), os.getenv('PASSWORD'), base_url)
    assert response.status_code == 200, f"[ERROR] {response.json()['detail']}"
    assert response.json()['token'] != "", '[ERROR] Bearer token came empty'
    
    yield response.json()['token'], base_url


def test_admin_has_user_management_permissions(setup_data):
    auth_token, base_url = setup_data

    get_all_users_response = get_all_users(auth_token, base_url)
    assert get_all_users_response.status_code == 200, '[ERROR] Could not get all users'
    assert len(get_all_users_response.json()) >= 1, '[ERROR] User list is empty'

    add_user_response = add_user(auth_token, add_user_payload(role='pending'), base_url)
    assert add_user_response.status_code == 200, '[ERROR] Could not add new user'
    assert add_user_response.json()['id'] is not None, '[ERROR] ID is empty'
    
    user_id = add_user_response.json()['id']

    change_user_role_response = change_user_role(auth_token, user_id, base_url)
    assert change_user_role_response.status_code == 200, '[ERROR] Could not change user role'
    assert change_user_role_response.json()['role'] == 'user', '[ERROR] Role was not updated'

    update_user_response = update_user_by_id(auth_token, user_id, update_user_payload(), base_url)
    assert update_user_response.status_code == 200, '[ERROR] Could not update user info'
    assert update_user_response.json()['email'] == 'updated.john.doe@test.com', '[ERROR] User email was not updated'

    get_user_chat_list_response = get_chat_list_by_user_id(auth_token, user_id, base_url)
    assert get_user_chat_list_response.status_code == 200, "[ERROR] Could not access user's chat list"

    delete_user_response = delete_user_by_id(auth_token, user_id, base_url)
    assert delete_user_response.status_code == 200, '[ERROR] Could not delete user'


def test_admin_config_changes_are_effective(setup_data):
    auth_token, base_url = setup_data
                                                                                                         
    change_default_user_role_response = update_admin_config(auth_token, update_admin_config_payload(True, True, "user", True, True), base_url)
    assert change_default_user_role_response.status_code == 200, '[ERROR] Unable to change default user role'
    assert change_default_user_role_response.json()["DEFAULT_USER_ROLE"] == "user", '[ERROR] Default user role is not the expected'
    
    signup_user_response = signup_user(auth_token, signup_user_payload(), base_url)
    assert signup_user_response.status_code == 200, f"[ERROR] {signup_user_response.json()['detail']}"
    assert signup_user_response.json()["role"] == "user", '[ERROR] User was not created with the expected role'

    delete_user_by_id(auth_token, signup_user_response.json()["id"], base_url)

