import allure
import requests
from src.data import Url, LoginCourierAnswer, Courier


@allure.suite("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_courier_can_login(self):
        payload = {'login': Courier.login, 'password': Courier.password}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.LOGIN_COURIER}", data=payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title("Курьер не может авторизоваться без логина")
    def test_courier_cannot_log_in_without_login(self):
        payload = {'password': Courier.password}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.LOGIN_COURIER}", data=payload)
        assert response.status_code == 400 and LoginCourierAnswer.answer_code_400 in response.text

    @allure.title("Курьер не может авторизоваться без пароля")
    def test_courier_cannot_log_in_without_password(self):
        payload = {'login': Courier.login}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.LOGIN_COURIER}", data=payload)
        assert response.status_code == 400 and LoginCourierAnswer.answer_code_400 in response.text

    @allure.title("Курьер не может авторизоваться с неверным логином")
    def test_invalid_courier_login(self):
        payload = {'login': 'Sacuraa', 'password': Courier.password}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.LOGIN_COURIER}", data=payload)
        assert response.status_code == 404 and LoginCourierAnswer.answer_code_404 in response.text

    @allure.title("Курьер не может авторизоваться с неверным паролем")
    def test_invalid_courier_password(self):
        payload = {'login': Courier.login, 'password': '1111'}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.LOGIN_COURIER}", data=payload)
        assert response.status_code == 404 and LoginCourierAnswer.answer_code_404 in response.text

    @allure.title("Курьер не может авторизоваться без логина и пароля")
    def test_courier_cannot_log_in_without_password_login(self):
        payload = {}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.LOGIN_COURIER}", data=payload)
        assert response.status_code == 400 and LoginCourierAnswer.answer_code_400 in response.text

    @allure.title("Курьер не может авторизоваться под несуществующим пользователем")
    def test_courier_cannot_log_in_nonexistent_user(self):
        payload = {'login': 'Saske', 'password': '5555'}
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.LOGIN_COURIER}", data=payload)
        assert response.status_code == 400 and LoginCourierAnswer.answer_code_400 in response.text
