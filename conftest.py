import pytest
import requests

from data.user_data import User
from data.handlers import *

@pytest.fixture()
def create_user():
    payload = User.create_data_user()
    login_data = payload.copy()
    response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Urls.MAIN_URL}{Handlers.DELETE_USER}", headers={'Authorization': f'{token}'})