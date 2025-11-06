import allure
from pages.main_page import MainPage
from urls import Urls

@allure.feature("Главная страница")
@allure.story("Раздел 'Услуги'")
class TestServicesSection:

    @allure.title("Проверка перехода в раздел 'Услуги'")
    def test_transition_to_services_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_services_button()
        main_page.wait_for_url_contains("#moreinfo")

        actual_url = driver.current_url
        expected_url = Urls.SERVICES_BLOCK
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        actual_title = main_page.get_services_title()
        expected_title = "услуги"
        assert actual_title == expected_title, f"Ожидался заголовок '{expected_title}', а получен '{actual_title}'"

        assert main_page.is_development_text_visible(), "Текст 'Разработка мобильных приложений' не отображается"
        assert main_page.is_outstaffing_text_visible(), "Текст 'Аутстаффинг IT-персонала' не отображается"
        assert main_page.is_consulting_text_visible(), "Текст 'Консалтинг' не отображается"
