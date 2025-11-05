import allure
from pages.main_page import MainPage
from urls import Urls

class TestAboutUsSection:

    @allure.title("Проверка перехода в раздел 'О нас'")
    def test_transition_to_about_us_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_about_us_button()
        main_page.wait_for_url_contains("#about")

        actual_url = driver.current_url
        expected_url = Urls.ABOUT_COMPANY_BLOCK
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        assert main_page.is_about_us_description_visible(), "Описание раздела 'О нас' не отображается"
        assert main_page.is_our_goal_visible(), "Блок 'Наша цель' не отображается"

        actual_title = main_page.get_about_us_title()
        expected_title = "О нас"
        assert actual_title == expected_title, f"Ожидался заголовок '{expected_title}', а получен '{actual_title}'"
