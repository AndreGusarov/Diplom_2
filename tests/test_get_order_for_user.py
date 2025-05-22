import allure
import requests

from data.ingredients_data import Ingredient
from data.handlers import *
from data.error_messages_list import ErrorMessages

allure.suite("Получение доступных заказов для пользователя")
class TestGetOrder:

    @allure.description("Получение доступных заказов авторизованного пользователя")
    @allure.title("Получение заказов")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        order = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}',headers=token, data=Ingredient.correct_ingredients_data)
        get_order = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}", headers=token)
        assert get_order.status_code == 200 and get_order.json()['orders'][0]['number'] == order.json()['order']['number']

    @allure.description("Получение доступных заказов для неавторизованного пользователя")
    @allure.title("Получение заказов")
    def test_get_order_without_auth(self):
        response = requests.get(f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}")
        assert response.status_code == 401 and response.json()['message'] == ErrorMessages.UNAUTHORIZED_MESSAGE