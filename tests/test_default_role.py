import os

import pytest
from dotenv import load_dotenv
from actions.auths import do_login, signup_user, get_admin_config
from actions.users import delete_user_by_id
from test_data.test_data import signup_user_payload


load_dotenv()


@pytest.fixture()
def setup_data(get_base_url):
    base_url = get_base_url

    response = do_login(os.getenv('EMAIL'), os.getenv('PASSWORD'), base_url)

    yield response.json()['token'], base_url


def test_user_is_created_with_default_role(setup_data):
    admin_auth_token, base_url = setup_data

    get_admin_config_response = get_admin_config(admin_auth_token, base_url)
    assert get_admin_config_response.status_code == 200, f"[ERROR] {get_admin_config_response.json()['detail']}"

    default_user_role = get_admin_config_response.json()['DEFAULT_USER_ROLE']

    signup_user_response = signup_user('', signup_user_payload(), base_url)
    assert signup_user_response.status_code == 200, f"[ERROR] {signup_user_response.json()['detail']}"
    assert signup_user_response.json()['id'] is not '', '[ERROR] ID is empty'
    assert signup_user_response.json()['token'] is not '', '[ERROR] Token is empty'
    assert signup_user_response.json()['role'] == default_user_role, '[ERROR] User was created with incorrect role'

    delete_user_by_id(admin_auth_token, signup_user_response.json()['id'], base_url)

