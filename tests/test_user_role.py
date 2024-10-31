import os

import pytest
from dotenv import load_dotenv

from actions.auths import do_login, add_user, update_admin_config, update_password, update_profile
from actions.chats import create_chat, get_chat_list_by_session_user, get_chat_by_id, get_chat_list_by_user_id
from actions.users import delete_user_by_id, change_user_role, update_settings_by_session_user
from test_data.test_data import *


load_dotenv()


@pytest.fixture()
def setup_data(get_base_url):
    base_url = get_base_url
    
    admin_login_response = do_login(os.getenv('EMAIL'), os.getenv('PASSWORD'), base_url)
    admin_auth_token = admin_login_response.json()['token']

    add_user_response = add_user(admin_auth_token, add_user_payload("user"), base_url)
    assert add_user_response.status_code == 200, f"[ERROR] {add_user_response.json()['detail']}"
    assert add_user_response.json()["id"] is not "", "[ERROR] ID is empty"
    assert add_user_response.json()["token"] is not "", "[ERROR] Token is empty"
    assert add_user_response.json()["role"] == "user", "[ERROR] User created with incorrect role"

    user_auth_token = add_user_response.json()["token"]
    user_id = add_user_response.json()["id"] 

    yield admin_auth_token, user_auth_token, user_id, base_url

    delete_user_by_id(admin_auth_token, user_id, base_url)


def test_user_can_login(setup_data):
    _, _, _, base_url = setup_data

    login_user_response = do_login(add_user_payload()["email"], add_user_payload()["password"], base_url)
    assert login_user_response.status_code == 200, '[ERROR] User could not log in'
    assert login_user_response.json()['token'] != "", '[ERROR] Bearer token came empty'


def test_user_cannot_change_own_role(setup_data):
    _, user_auth_token, user_id, base_url = setup_data

    change_user_role_response = change_user_role(user_auth_token, user_id, base_url)
    assert change_user_role_response.status_code == 401, "[ERROR] User was allowed to change its own role"


def test_user_has_chat_permissions(setup_data):
    _, user_auth_token, _, base_url = setup_data

    create_chat_response = create_chat(user_auth_token, create_empty_chat_payload(), base_url)
    assert create_chat_response.status_code == 200, "[ERROR] User could not create chat"

    get_chats_response = get_chat_list_by_session_user(user_auth_token, base_url)
    assert get_chats_response.status_code == 200, "[ERROR] User could not access own chat list"


def test_user_does_not_have_access_to_other_users_chats(setup_data):
    admin_auth_token, user_auth_token, _, base_url = setup_data

    add_second_user_response = add_user(admin_auth_token, add_second_user_payload("user"), base_url)
    assert add_second_user_response.status_code == 200, f"[ERROR] {add_second_user_response.json()['detail']}"

    second_user_auth_token = add_second_user_response.json()["token"]
    second_user_id = add_second_user_response.json()["id"] 

    create_chat_as_second_user_response = create_chat(second_user_auth_token, create_empty_chat_payload(), base_url)
    assert create_chat_as_second_user_response.status_code == 200, f"[ERROR] {create_chat_as_second_user_response.json()['detail']}"

    second_user_chat_id = create_chat_as_second_user_response.json()["id"]

    get_another_users_chat_response = get_chat_by_id(user_auth_token, second_user_chat_id, base_url)
    assert get_another_users_chat_response.status_code == 401, "[ERROR] User was able to access another user's chat"

    get_another_users_chat_list_response = get_chat_list_by_user_id(user_auth_token, second_user_id, base_url)
    assert get_another_users_chat_list_response.status_code == 401, "[ERROR] User was able to access another user's chat list"

    delete_user_by_id(admin_auth_token, second_user_id, base_url)


def test_user_can_change_own_info(setup_data):
    _, user_auth_token, _, base_url = setup_data

    update_profile_response = update_profile(user_auth_token, update_profile_payload(), base_url)
    assert update_profile_response.status_code == 200, "[ERROR] User was not able to update its profile"
    assert update_profile_response.json()["name"] == update_profile_payload()["name"], "[ERROR] User name is not the expected"
    assert update_profile_response.json()["profile_image_url"] == update_profile_payload()["profile_image_url"], "[ERROR] User image is not the expected"

    update_password_response = update_password(user_auth_token, update_password_payload(), base_url)
    assert update_password_response.status_code == 200, "[ERROR] User was not able to update its password"

    login_with_new_password_response = do_login(add_user_payload()["email"], update_password_payload()["new_password"], base_url)
    assert login_with_new_password_response.status_code == 200, "[ERROR] User could not login with new password"


def test_user_can_change_own_ui_settings(setup_data):
    _, user_auth_token, _, base_url = setup_data

    update_user_settings_response = update_settings_by_session_user(user_auth_token, update_user_settings_payload(), base_url)
    assert update_user_settings_response.status_code == 200, "[ERROR] User could not update UI settings"
    assert update_user_settings_response.json()["ui"]["landingPageMode"] == update_user_settings_payload()["ui"]["landingPageMode"] , "[ERROR] User's landing page mode was not updated"
    assert update_user_settings_response.json()["ui"]["chatDirection"] == update_user_settings_payload()["ui"]["chatDirection"] , "[ERROR] User's chat direction was not updated"

