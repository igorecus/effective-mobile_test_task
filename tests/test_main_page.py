import allure
from pages.main_page import MainPage

@allure.feature("Главная страница")
@allure.story("Открытие страницы")
class TestMainPage:

    @allure.title("Проверка открытия главной страницы")
    def test_open_page(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()

        actual_url = driver.current_url
        expected_url = "https://effective-mobile.ru/"
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        actual_text = main_page.get_page_logo()
        expected_text = "Effective Mobile"
        assert actual_text == expected_text, f"Ожидался текст '{expected_text}', а получен '{actual_text}'"

        assert main_page.is_page_title_visible(), "Заголовок 'Разработка мобильных приложений' не отображается"
        assert main_page.is_more_info_button_visible(), "Кнопка 'Подробнее' не отображается"
        assert main_page.is_more_info_button_clickable(), "Кнопка 'Подробнее' не кликабельна"
