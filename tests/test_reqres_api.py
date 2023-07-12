import allure
from jsonschema.validators import validate

from utils.helper import load_json_schema


@allure.tag('api')
@allure.title('Создание пользователя')
def test_create_user(reqres):
    response = reqres.post("/api/users", {"name": "Dmitriy", "job": "president"})

    assert response.status_code == 201
    validate(instance=response.json(), schema=load_json_schema('user_create.json'))
    assert response.json()["name"] == "Dmitriy"
    assert response.json()["job"] == "president"


@allure.tag('api')
@allure.title('Обновление данных пользователя')
def test_update_user_by_put(reqres):
    response = reqres.put("/api/users/2", {"name": "Viktior", "job": "test"})

    assert response.status_code == 200
    validate(instance=response.json(), schema=load_json_schema('user_update.json'))
    assert response.json()["name"] == "Viktior"
    assert response.json()["job"] == "test"


@allure.tag('api')
@allure.title('Регистрация пользователя')
def test_register_success(reqres):
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = reqres.post(url=f'/api/register', data=data)

    assert response.status_code == 200
    validate(instance=response.json(), schema=load_json_schema('post_register_success.json'))


@allure.tag('api')
@allure.title('Удаление пользователя')
def test_delete_user(reqres):
    delete_user = reqres.delete("/api/users/2")

    assert delete_user.status_code == 204


@allure.tag('api')
@allure.title('Регистрация с ошибкой')
def test_login_unsuccess(reqres):
    response = reqres.post("/api/register", {"email": "5678@gmail.com"})

    assert response.status_code == 400
    validate(instance=response.json(), schema=load_json_schema('login_unsuccess.json'))
    assert response.json()['error'] == 'Missing password'
