class Url:
    PAGE_SCOOTER = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = "/api/v1/courier"
    LOGIN_COURIER = '/api/v1/courier/login'
    CREATE_ORDER = '/api/v1/orders'
    LIST_OF_ORDERS = '/api/v1/orders'


class Courier:
    login = "Sakura"
    password = "1234"
    firstName = "Sakura"


class InfoForOrder:
    firstName = "Sakura"
    lastName = "Haruno"
    address = "Ninja Blvd, 7 apt"
    metroStation = 2
    phone = "+7 937 133 78 87"
    rentTime = 2
    deliveryDate = "2024-10-09"
    comment = "Urgent delivery!"


class CreateCourierAnswer:
    answer_code_201 = '{"ok":true}'
    answer_code_400 = 'Недостаточно данных для создания учетной записи'
    answer_code_409 = 'Этот логин уже используется'


class LoginCourierAnswer:
    answer_code_400 = 'Недостаточно данных для входа'
    answer_code_404 = 'Учетная запись не найдена'
    