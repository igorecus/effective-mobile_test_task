import allure
from pages.main_page import MainPage
from urls import Urls

@allure.feature("Главная страница")
@allure.story("Футер")
class TestFooterSection:

    @allure.title("Проверка отображения элементов футера")
    def test_footer_elements_visibility(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_contacts_button()
        main_page.wait_for_url_contains("#contacts")

        main_page.scroll_to_footer_section()

        assert main_page.is_footer_title_visible(), "Логотип футера не отображается"
        assert main_page.is_company_info_visible(), "Юридическая информация компании не отображается"
        assert main_page.is_copyright_visible(), "Информация о копирайте не отображается"
        assert main_page.is_footer_privacy_link_visible(), "Ссылка на Политику конфиденциальности не отображается"

    @allure.title("Проверка перехода к главной странице при клике на логотип в футере")
    def test_footer_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_contacts_button()
        main_page.wait_for_url_contains("#contacts")

        main_page.scroll_to_footer_section()
        main_page.click_footer_title()
        main_page.wait_for_url_contains("#main")

        actual_url = driver.current_url
        expected_url = Urls.MAIN
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

    @allure.title("Проверка корректности ссылки на Политику конфиденциальности в футере")
    def test_footer_privacy_policy_link_href(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_contacts_button()
        main_page.wait_for_url_contains("#contacts")

        main_page.scroll_to_footer_section()

        privacy_href = main_page.get_footer_privacy_link_href()
        assert privacy_href == Urls.PRIVACY_POLICY, \
            f"Ожидался href '{Urls.PRIVACY_POLICY}', а получен '{privacy_href}'"
