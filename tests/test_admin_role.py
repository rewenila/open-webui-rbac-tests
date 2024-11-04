import os

import pytest
from dotenv import load_dotenv

from actions.auths import do_login, signup_user, add_user, update_admin_config
from actions.knowledge import get_all_knowledge, create_knowledge, update_knowledge_by_id, delete_knowledge_by_id
from actions.chats import get_chat_list_by_user_id
from actions.models import get_all_models, add_model, update_model_by_id, delete_model_by_id
from actions.prompts import get_all_prompts, create_prompt, update_prompt_by_command, delete_prompt_by_command
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


def test_admin_has_model_management_permissions(setup_data):
    auth_token, base_url = setup_data

    add_model_response = add_model(auth_token, add_model_payload(), base_url)
    assert add_model_response.status_code == 200, '[ERROR] Could not add model'
    assert add_model_response.json()["id"] == add_model_payload()["id"], '[ERROR] Model ID is not the expected'
    assert add_model_response.json()["name"] == add_model_payload()["name"], '[ERROR] Model name is not the expected'
    assert add_model_response.json()["meta"]["description"] == add_model_payload()["meta"]["description"], '[ERROR] Model description is not the expected'
    assert add_model_response.json()["meta"]["profile_image_url"] == add_model_payload()["meta"]["profile_image_url"], '[ERROR] Model image is not the expected'

    get_all_models_response = get_all_models(auth_token, base_url)
    assert get_all_models_response.status_code == 200, '[ERROR] Could not get all models'
    assert len(get_all_models_response.json()) >= 1, "[ERROR] Model list is empty"

    update_model_response = update_model_by_id(auth_token, add_model_payload()["id"], update_model_payload(), base_url)
    assert update_model_response.status_code == 200, '[ERROR] Could not update model'
    assert update_model_response.json()["name"] == update_model_payload()["name"], '[ERROR] Model name was not updated'
    assert update_model_response.json()["meta"]["description"] == update_model_payload()["meta"]["description"], '[ERROR] Model description was not updated'
    assert update_model_response.json()["meta"]["profile_image_url"] == update_model_payload()["meta"]["profile_image_url"], '[ERROR] Model image was not updated'

    delete_model_response = delete_model_by_id(auth_token, add_model_payload()["id"], base_url)
    assert delete_model_response.status_code == 200, '[ERROR] Could not delete model'


def test_admin_has_prompt_management_permissions(setup_data):
    auth_token, base_url = setup_data

    create_prompt_response = create_prompt(auth_token, create_prompt_payload(), base_url)
    assert create_prompt_response.status_code == 200, '[ERROR] Could not create prompt'
    assert create_prompt_response.json()["user_id"] is not None, "[ERROR] User ID is empty"
    assert create_prompt_response.json()["command"] == create_prompt_payload()["command"], '[ERROR] Prompt command is not the expected'
    assert create_prompt_response.json()["title"] == create_prompt_payload()["title"], '[ERROR] Prompt title is not the expected'
    assert create_prompt_response.json()["content"] == create_prompt_payload()["content"], '[ERROR] Prompt content is not the expected'

    get_all_prompts_response = get_all_prompts(auth_token, base_url)
    assert get_all_prompts_response.status_code == 200, '[ERROR] Could not get all prompts'
    assert len(get_all_prompts_response.json()) >= 1, "[ERROR] Prompt list is empty"

    update_prompt_response = update_prompt_by_command(auth_token, create_prompt_payload()["command"], update_prompt_payload(), base_url)
    assert update_prompt_response.status_code == 200, '[ERROR] Could not update prompt'
    assert update_prompt_response.json()["title"] == update_prompt_payload()["title"], '[ERROR] Prompt title was not updated'
    assert update_prompt_response.json()["content"] == update_prompt_payload()["content"], '[ERROR] Prompt content was not updated'

    delete_prompt_response = delete_prompt_by_command(auth_token, create_prompt_payload()["command"], base_url)
    assert delete_prompt_response.status_code == 200, '[ERROR] Could not delete prompt'


def test_admin_has_knowledge_management_permissions(setup_data):
    auth_token, base_url = setup_data

    create_knowledge_response = create_knowledge(auth_token, create_knowledge_payload(), base_url)
    assert create_knowledge_response.status_code == 200, '[ERROR] Could not create knowledge'
    assert create_knowledge_response.json()["id"] is not None, "[ERROR] ID is empty"
    assert create_knowledge_response.json()["name"] == create_knowledge_payload()["name"], '[ERROR] Knowledge name is not the expected'
    assert create_knowledge_response.json()["description"] == create_knowledge_payload()["description"], '[ERROR] Knowledge description is not the expected'

    get_all_knowledges_response = get_all_knowledge(auth_token, base_url)
    assert get_all_knowledges_response.status_code == 200, '[ERROR] Could not get all knowledge'
    assert len(get_all_knowledges_response.json()) >= 1, "[ERROR] Knowledge list is empty"

    update_knowledge_response = update_knowledge_by_id(auth_token, create_knowledge_response.json()["id"], update_knowledge_payload(), base_url)
    assert update_knowledge_response.status_code == 200, '[ERROR] Could not update knowledge'
    assert update_knowledge_response.json()["name"] == update_knowledge_payload()["name"], '[ERROR] Knowledge name was not updated'
    assert update_knowledge_response.json()["description"] == update_knowledge_payload()["description"], '[ERROR] Knowledge description was not updated'

    delete_knowledge_response = delete_knowledge_by_id(auth_token, create_knowledge_response.json()["id"], base_url)
    assert delete_knowledge_response.status_code == 200, '[ERROR] Could not delete knowledge'


def test_admin_config_changes_are_effective(setup_data):
    auth_token, base_url = setup_data
                                                                                                         
    change_default_user_role_response = update_admin_config(auth_token, update_admin_config_payload(True, True, "user", True, True), base_url)
    assert change_default_user_role_response.status_code == 200, '[ERROR] Unable to change default user role'
    assert change_default_user_role_response.json()["DEFAULT_USER_ROLE"] == "user", '[ERROR] Default user role is not the expected'
    
    signup_user_response = signup_user(auth_token, signup_user_payload(), base_url)
    assert signup_user_response.status_code == 200, f"[ERROR] {signup_user_response.json()['detail']}"
    assert signup_user_response.json()["role"] == "user", '[ERROR] User was not created with the expected role'

    delete_user_by_id(auth_token, signup_user_response.json()["id"], base_url)

