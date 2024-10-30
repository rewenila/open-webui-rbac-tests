import os

import pytest
from dotenv import load_dotenv


load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--ENV", action="store", default="local", help="Select environment")


@pytest.fixture(autouse=True)
def get_base_url(request):
    base_url = ""
    env = request.config.getoption('--ENV')
    print(env)

    match env:
        case 'local':
            base_url = f"{os.getenv('LOCAL_URL')}:{os.getenv('PORT')}"
        case 'remote':
            base_url = f"{os.getenv('REMOTE_URL')}"
    print(base_url)

    yield base_url

