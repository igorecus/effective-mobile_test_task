import allure
from pages.main_page import MainPage
from urls import Urls

@allure.feature("Главная страница")
@allure.story("Раздел 'О нас'")
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

    @allure.title("Проверка отображения всех карточек и заголовка в разделе 'Почему мы'")
    def test_all_why_we_cards_visibility(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_about_us_button()
        main_page.wait_for_url_contains("#about")

        main_page.scroll_to_why_we_section()

        assert main_page.is_why_we_title_visible(), "Заголовок 'Почему мы' не отображается"
        assert main_page.is_card_1_visible(), "Карточка 'Сокращение рисков найма' не отображается"
        assert main_page.is_card_2_visible(), "Карточка 'Широкий выбор специалистов' не отображается"
        assert main_page.is_card_3_visible(), "Карточка 'Эффективное распределение ресурсов' не отображается"
        assert main_page.is_card_4_visible(), "Карточка 'Быстрое привлечение специалистов' не отображается"
        assert main_page.is_card_5_visible(), "Карточка 'Отсутствие бумажной волокиты' не отображается"
        assert main_page.is_link_to_application_form_visible(), \
            "Кнопка 'Оставить заявку на сотрудничество' не отображается"

    @allure.title("Проверка перехода в раздел 'Контакты' через кнопку 'Оставить заявку на сотрудничество'")
    def test_link_to_application_form_redirects_to_contacts(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_about_us_button()
        main_page.wait_for_url_contains("#about")

        main_page.scroll_to_application_form_link()
        main_page.click_link_to_application_form()
        main_page.wait_for_url_contains("#contacts")

        actual_url = driver.current_url
        expected_url = Urls.CONTACTS_BLOCK
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        assert main_page.is_contact_form_visible(), "Форма заявки не отображается после перехода"
