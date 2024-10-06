import allure
import requests
from src.data import Url, InfoForOrder


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с цветом BLACK")
    def test_create_order_with_black_color(self):
        payload = {
            "firstName": InfoForOrder.firstName,
            "lastName": InfoForOrder.lastName,
            "address": InfoForOrder.address,
            "metroStation": InfoForOrder.metroStation,
            "phone": InfoForOrder.phone,
            "rentTime": InfoForOrder.rentTime,
            "deliveryDate": InfoForOrder.deliveryDate,
            "comment": InfoForOrder.comment,
            "color": ["BLACK"]
        }
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_ORDER}", json=payload)
        assert response.status_code == 201 and 'track' in response.json()


    @allure.title("Создание заказа с цветом GREY")
    def test_create_order_with_grey_color(self):
        payload = {
            "firstName": InfoForOrder.firstName,
            "lastName": InfoForOrder.lastName,
            "address": InfoForOrder.address,
            "metroStation": InfoForOrder.metroStation,
            "phone": InfoForOrder.phone,
            "rentTime": InfoForOrder.rentTime,
            "deliveryDate": InfoForOrder.deliveryDate,
            "comment": InfoForOrder.comment,
            "color": ["GREY"]
        }
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_ORDER}", json=payload)
        assert response.status_code == 201 and 'track' in response.json()

    @allure.title("Создание заказа с цветами BLACK и GREY")
    def test_create_order_with_black_and_grey_colors(self):
        payload = {
            "firstName": InfoForOrder.firstName,
            "lastName": InfoForOrder.lastName,
            "address": InfoForOrder.address,
            "metroStation": InfoForOrder.metroStation,
            "phone": InfoForOrder.phone,
            "rentTime": InfoForOrder.rentTime,
            "deliveryDate": InfoForOrder.deliveryDate,
            "comment": InfoForOrder.comment,
            "color": ["BLACK", "GREY"]
        }
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_ORDER}", json=payload)
        assert response.status_code == 201 and 'track' in response.json()

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self):
        payload = {
            "firstName": InfoForOrder.firstName,
            "lastName": InfoForOrder.lastName,
            "address": InfoForOrder.address,
            "metroStation": InfoForOrder.metroStation,
            "phone": InfoForOrder.phone,
            "rentTime": InfoForOrder.rentTime,
            "deliveryDate": InfoForOrder.deliveryDate,
            "comment": InfoForOrder.comment
        }
        response = requests.post(f"{Url.PAGE_SCOOTER}{Url.CREATE_ORDER}", json=payload)
        assert response.status_code == 201 and 'track' in response.json()

