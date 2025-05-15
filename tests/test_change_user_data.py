import allure
import requests

from data.user_data import User
from data.handlers import *
from conftest import create_user

@allure.suite('Изменение данных пользовователя')
class TestChangeUserData:
    
    @allure.description("Успешное изменение поля email для авторизованного пользователя")
    @allure.title("Изменение поля email для авторизованного пользователя")
    def test_change_user_email_with_auth(self, create_user):
        payload = {'email': User.create_data_user()["email"]}
        token = {'Authorization': create_user[3]}
        response = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert response.status_code == 200 and response.json()['user']['email'] == payload["email"]

    @allure.description("Успешное изменение поля password для авторизованного пользователя")
    @allure.title("Изменение поля password для авторизованного пользователя")
    def test_change_user_password_with_auth(self, create_user):
        payload = {'password': User.create_data_user()["password"]}
        token = {'Authorization': create_user[3]}
        response = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description("Успешное изменение поля name для авторизованного пользователя")
    @allure.title("Изменение поля name для авторизованного пользователя")
    def test_change_user_name_with_auth(self, create_user):
        payload = {'name': User.create_data_user()["name"]}
        token = {'Authorization': create_user[3]}
        response = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", headers=token, data=payload)
        assert response.status_code == 200 and response.json()['user']['name'] == payload["name"]

    @allure.description("Alert при попытке смены даных пользователя без авторизации")
    @allure.title("Изменение данных пользователя без авторизацией")
    def test_change_user_data_without_auth(self):
        response = requests.patch(f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}", data=User.create_data_user())
        assert response.status_code == 401 and response.json()['message'] == 'You should be authorised'