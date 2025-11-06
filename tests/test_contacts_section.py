import allure
from pages.main_page import MainPage
from helper import generate_registration_data
from urls import Urls

@allure.feature("Главная страница")
@allure.story("Раздел 'Контакты'")
class TestContactsSection:

    @allure.title("Проверка перехода в раздел 'Контакты'")
    def test_transition_to_contacts_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_contacts_button()
        main_page.wait_for_url_contains("#contacts")

        actual_url = driver.current_url
        expected_url = Urls.CONTACTS_BLOCK
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        actual_title = main_page.get_contacts_title()
        expected_title = "контакты"
        assert actual_title == expected_title, f"Ожидался заголовок '{expected_title}', а получен '{actual_title}'"

        actual_call_to_action_title = main_page.get_call_to_action_text()
        expected_call_to_action_title = "Остались вопросы?\nОставьте заявку\nна консультацию"
        assert actual_call_to_action_title == expected_call_to_action_title, \
            f"Ожидался заголовок '{expected_call_to_action_title}', а получен '{actual_call_to_action_title}'"

        assert main_page.is_contact_form_visible(), "Форма заявки не отображается"

    @allure.title("Проверка отображения ссылок в разделе 'Контакты'")
    def test_contacts_links_visibility(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_contacts_button()
        main_page.wait_for_url_contains("#contacts")

        assert main_page.is_it_support_link_visible(), "Ссылка на IT поддержку не отображается"
        assert main_page.is_telegram_link_visible(), "Ссылка на Telegram не отображается"
        assert main_page.is_email_link_visible(), "Ссылка на Email не отображается"
        assert main_page.is_privacy_link_visible(), "Ссылка на Политику конфиденциальности не отображается"

    @allure.title("Проверка корректности href ссылок в разделе 'Контакты'")
    def test_contacts_links_href(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_contacts_button()
        main_page.wait_for_url_contains("#contacts")

        it_support_href = main_page.get_it_support_link_href()
        assert it_support_href == Urls.TELEGRAM_SUPPORT, \
            f"Ожидался href '{Urls.TELEGRAM_SUPPORT}', а получен '{it_support_href}'"

        telegram_href = main_page.get_telegram_link_href()
        assert telegram_href == Urls.COFOUNDER_TELEGRAM_LINK, \
            f"Ожидался href '{Urls.COFOUNDER_TELEGRAM_LINK}', а получен '{telegram_href}'"

        email_href = main_page.get_email_link_href()
        assert email_href == Urls.EMAIL_SUPPORT, \
            f"Ожидался href '{Urls.EMAIL_SUPPORT}', а получен '{email_href}'"

        privacy_href = main_page.get_privacy_link_href()
        assert privacy_href == Urls.PRIVACY_POLICY, \
            f"Ожидался href '{Urls.PRIVACY_POLICY}', а получен '{privacy_href}'"

    @allure.title("Проверка заполнения и отправки формы в разделе 'Контакты'")
    def test_contact_form_submission(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_contacts_button()
        main_page.wait_for_url_contains("#contacts")

        name, telegram_nick, phone, additional_info = generate_registration_data()

        main_page.fill_first_name_field(name)
        main_page.fill_phone_field(phone)
        main_page.fill_telegram_field(telegram_nick)
        main_page.fill_additional_info_field(additional_info)

        main_page.click_send_button()

        assert main_page.is_success_message_visible(), "Сообщение об успешной отправке не отображается"
