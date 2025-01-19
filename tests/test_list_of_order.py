import allure
import requests
from src.data import Url


@allure.suite("Список заказов")
class TestListOfOrders:

    @allure.title("Возвращается список заказов")
    def test_get_list_order(self):
        response = requests.get(f"{Url.PAGE_SCOOTER}{Url.LIST_OF_ORDERS}")
        assert response.status_code == 200 and 'orders' in response.json()
