import allure
from pages.main_page import MainPage
from helper import generate_registration_data
from urls import Urls

@allure.feature("Главная страница")
@allure.story("Раздел 'Специалисты'")
class TestSpecialistsSection:

    @allure.title("Проверка перехода в раздел 'Специалисты'")
    def test_transition_to_specialists_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_choose_a_super_hero_button()
        main_page.wait_for_url_contains("#specialists")

        actual_url = driver.current_url
        expected_url = Urls.SPECIALISTS_BLOCK
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        actual_title = main_page.get_our_stack_title()
        expected_title = "Наш стек"
        assert actual_title == expected_title, f"Ожидался заголовок '{expected_title}', а получен '{actual_title}'"

        assert main_page.is_about_us_description_visible(), "Заголовок  'Android (нативная разработка)' не отображается"
        assert main_page.is_about_us_description_visible(), "Заголовок  'iOS (нативная разработка)' не отображается"
        assert main_page.is_about_us_description_visible(), \
            "Заголовок  'Flutter (кросплатформенная разработка)' не отображается"

    @allure.title("Проверка отображения раздела 'Подберем для вас'")
    def test_select_it_for_you_section_visibility(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.scroll_to_select_it_for_you_section()

        assert main_page.is_select_it_for_you_title_visible(), "Заголовок 'Подберем для вас' не отображается"

        actual_title = main_page.get_select_it_for_you_title()
        expected_title = "подберем для вас"
        assert actual_title == expected_title, \
            f"Ожидался заголовок содержащий '{expected_title}', а получен '{actual_title}'"

    @allure.title("Проверка отображения нескольких карточек специалистов в разделе 'Подберем для вас'")
    def test_all_specialist_cards_visibility(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.scroll_to_select_it_for_you_section()

        assert main_page.is_mobile_dev_card_visible(), "Карточка 'Mobile-разработчик' не отображается"
        assert main_page.is_business_analyst_card_visible(), "Карточка 'Бизнес-аналитик' не отображается"
        assert main_page.is_qa_auto_card_visible(), "Карточка 'QA автоматизатор' не отображается"
        assert main_page.is_php_dev_card_visible(), "Карточка 'PHP-разработчик' не отображается"
        assert main_page.is_1c_analyst_card_visible(), "Карточка '1С-аналитик' не отображается"
        assert main_page.is_apply_button_visible(), "Кнопка 'Оставить заявку на консультацию' не отображается"

    @allure.title("Проверка открытия формы 'Остались вопросы?' через кнопку 'Оставить заявку на консультацию'")
    def test_open_any_other_question_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.scroll_to_submit_request_for_consult_button()
        main_page.click_submit_request_for_consult_button()

        assert main_page.is_popup_any_other_question_visible(), \
            "Всплывающее окно 'Остались вопросы?' не открылось"

    @allure.title("Проверка заполнения и отправки формы 'Остались вопросы?'")
    def test_submit_any_other_question_form(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.scroll_to_submit_request_for_consult_button()
        main_page.click_submit_request_for_consult_button()

        assert main_page.is_popup_any_other_question_visible(), \
            "Всплывающее окно 'Остались вопросы?' не открылось"

        name, telegram_nick, _, _ = generate_registration_data()

        main_page.fill_popup_first_name_field(name)
        main_page.fill_popup_telegram_field(telegram_nick)
        main_page.click_popup_submit_button()

        assert main_page.is_popup_success_message_visible(), \
            "Сообщение об успешной отправке не отображается в попапе"

    @allure.title("Проверка закрытия формы 'Остались вопросы?'")
    def test_close_any_other_question_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.scroll_to_submit_request_for_consult_button()
        main_page.click_submit_request_for_consult_button()

        assert main_page.is_popup_any_other_question_visible(), \
            "Всплывающее окно 'Остались вопросы?' не открылось"

        main_page.close_popup_any_other_question()

        assert main_page.is_popup_any_other_question_closed(), \
            "Всплывающее окно 'Остались вопросы?' не закрылось"
