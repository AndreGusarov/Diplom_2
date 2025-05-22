import allure
import requests

from data.ingredients_data import Ingredient
from data.handlers import *
from data.error_messages_list import ErrorMessages

@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.description("Создание заказа авторизованным пользователем")
    @allure.title("Создание заказа")
    def test_create_order_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}',headers=token, data= Ingredient.correct_ingredients_data)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.description("Создание заказа неавторизованным пользователем")
    @allure.title("Создание заказа")
    def test_create_order_without_auth(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}',data=Ingredient.correct_ingredients_data)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.description("Создание заказа без ингредиентов")
    @allure.title("Создание заказа")
    def test_create_order_without_ingredients(self):
        resonse = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}')
        assert resonse.status_code == 400 and resonse.json()['message'] == ErrorMessages.NO_INGREDIENTS_MESSAGE

    @allure.description("Создание заказа c невалидным хешем ингредиентов")
    @allure.title("Создание заказа")
    def test_create_order_with_invalid_hash(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}', data=Ingredient.incorrect_ingredients_data)
        assert response.status_code == 500 and ErrorMessages.INTERNAL_SERVER_ERROR_MESSAGE in response.text #Проверять, что сервер пятисотит, совсем не ок, но в спеке api-documentation.pdf это ожидаемое поведение :)



    

    

