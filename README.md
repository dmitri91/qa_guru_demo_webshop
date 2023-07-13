## Проект автотестов  UI + API 

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/logo/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>


<!-- Тест кейсы -->

## Покрытый функционал

1. [DemoWebShop](https://demowebshop.tricentis.com/) - UI
    - Регистрация пользователя
    - Авторизация пользователя
    - Поиск товара
    - Удаление товара из корзины
    - Добавление товара в корзину
2. [reqres](https://reqres.in/) - API
   - Регистрация пользователя 
   - Обновление данных пользователя
   - Создание пользователя
   - Обновление данных пользователя
   - Удаление пользователя
   - Регистрация с невалидными данными

## Запуск тестов

### [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/005-diploma_project_ld/)

Для запуска тестов выбрать "Собрать сейчас"

![Jenkins](/images/screenshot/jenkins.png)

Результат о прохождении тестов присылается в телеграм, со ссылкой на Allure отчет.

![Telegram](/images/screenshot/teleg.png)

### __Примеры Allure отчётов:__ 

#### [Allure Report](https://jenkins.autotests.cloud/job/005-diploma_project_ld/8/allure/)

UI-тесты

![Allure UI](/images/screenshot/ui.png)

API-тесты

![Allure API](/images/screenshot/api.png)

Пример видео прохождения теста

![Allure vid](/images/screenshot/del.gif)

### __Интеграции с другими сервисами:__ 
[Allure TestOps](https://allure.autotests.cloud/launch/26950/tree?treeId=6826&search=)

![Allure TestOps](/images/screenshot/allureTestOps.png)

[Jira](https://jira.autotests.cloud/browse/HOMEWORK-783)

![Allure TestOps](/images/screenshot/jira.png)
