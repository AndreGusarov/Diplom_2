import allure
import requests

from data.user_data import User
from data.handlers import *

@allure.suite('Авторизация пользователя')
class TestLogin:
     @allure.description('Успешный вход для зарегистрированного пользователя')
     @allure.title('Авторизация под пользователем, который есть в системе')
     def test_login_user(self):
          response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.correct_credentials)
          assert response.status_code == 200 and response.json().get('success') == True
          
     @allure.description('Alet при неверном логине/пароле')
     @allure.title('Авторизация с неверным логином или паролем')
     def test_login_user_eror(self):
          response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}',data=User.negative_credentials)
          assert response.status_code == 401 and response.json().get('success') == False
     