# Автоматизация UI-тестирования главной страницы effective-mobile.ru

## Описание
Проект реализует UI-тесты для проверки навигации по основным блокам главной страницы сайта effective-mobile.ru с использованием Selenium, pytest и Allure. Тесты покрывают клики по ссылкам "О нас", "Контакты" и "Политика конфиденциальности", проверяя локаторы и целевые URL/фрагменты.

- **Фреймворк**: Selenium + Pytest + Allure
- **Паттерн**: Page Object Model
- **Python**: 3.10

## Установка и запуск локально
1. Клонируйте репозиторий c помощь ю команды git clone в вашу IDE: 
> https://github.com/igorecus/effective-mobile_test_task

2. Установите зависимости:
> pip install -r requirements.txt

3. Для запуска всех тестов используйте команду в терминале:

> pytest tests/test_main_functionality.py::TestMainFunctionality::test_open_page

3.1 Для запуска конкретного теста (например, test_open_page):

> pytest tests/test_main_functionality.py::TestMainFunctionality::test_open_page

## Структура проекта
- `pages/`: Page Objects (base_page.py, main_page.py)
- `locators/`: Локаторы (main_page_locators.py)
- `tests/`: Тесты (test_main_page.py)
- `conftest.py`: Фикстуры (драйвер)
- `requirements.txt`: Зависимости
- `Dockerfile`: Контейнер для тестов

## Лучшие практики
- **Ожидания**: WebDriverWait для стабильности.
- **Параметризация**: Один тест на все ссылки.
- **Allure**: Динамические заголовки, отчет в allure-results.
- **Docker**: Автоматическая установка Chrome и драйвера.

Если тесты падают (изменения на сайте), обновите локаторы в main_page.py.