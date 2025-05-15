from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    correct_credentials = {
        "email": 'test_user13@mail.ru',
        "password": "password"}

    negative_credentials = {
        "email": 'test_user13.ru',
        "password": "password"}

    duplicate_credentials = {
        "email": 'test_user13@mail.ru',
        "password": "password",
        "name": "Username"}

    without_email_credentials = {
        "email": '',
        "password": "password",
        "name": "Username"}

    without_password_credentials = {
        "email": 'test_user13@mail.ru',
        "password": "",
        "name": "Username"}

    without_name_credentials = {
        "email": 'test_user13@mail.ru',
        "password": "password",
        "name": ""}

    update_credentials = {
        "email": 'test_user13@mail.ru',
        "password": "password",
        "name": "Test"}