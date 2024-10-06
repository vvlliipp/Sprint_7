import allure
import requests
from src.data import Url, CreateCourierAnswer, Courier
from src.helpers import RegisterNewCourier


@allure.suite("Создание курьера")
class TestCreateCourier:
    @allure.title("Курьера можно создать")
    def test_create_courier(self):
        payload = RegisterNewCourier.register_new_courier()
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_COURIER}", json=payload)
        assert response.status_code == 201 and CreateCourierAnswer.answer_code_201 == response.text

    @allure.title("Создание двух одинаковых курьеров")
    def test_creating_two_couriers(self):
        payload = RegisterNewCourier.register_new_courier()
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_COURIER}", data=payload)
        response2 = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_COURIER}", data=payload)
        assert response2.status_code == 409 and CreateCourierAnswer.answer_code_409 in response.text

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self):
        payload = {'password':Courier.password, 'first_name': Courier.firstName}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_COURIER}", data=payload)
        assert response.status_code == 400 and CreateCourierAnswer.answer_code_400 in response.text

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self):
        payload = {'login': Courier.login, 'first_name': Courier.firstName}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_COURIER}", data=payload)
        assert response.status_code == 400 and CreateCourierAnswer.answer_code_400 in response.text





