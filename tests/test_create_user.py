import allure
import pytest
import requests

from data.user_data import User
from data.handlers import *

@allure.suite('Создание пользователя')
class TestCreateUser():

    @allure.description('Успешное оздание нового пользователя')
    @allure.title('Создание нового пользователя')
    def test_create_new_user_success(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=User.create_data_user())
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.description('Alert при создании уже существующего пользователя')
    @allure.title('Создание пользователя, который уже зарегестрирован')
    def test_create_duplicate_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=User.duplicate_credentials)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.description('Alert при создании пользователя с некорректыми данными')
    @allure.title('Создание пользователя без одного из обязательных полей')
    @pytest.mark.parametrize("user_data", [User.without_email_credentials, User.without_password_credentials, User.without_name_credentials])
    def test_create_user_required_fields(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text

