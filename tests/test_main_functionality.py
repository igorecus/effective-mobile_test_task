import allure

from helper import generate_registration_data
from pages.main_page import MainPage
from urls import Urls


class TestMainFunctionality:

    # Проверки для проверки открытия главной страницы/главного окна

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

        actual_page_title = main_page.get_page_title()
        expected_page_title = "Разработка мобильных приложений"
        assert actual_page_title == expected_page_title, \
            f"Ожидался текст '{expected_page_title}', а получен '{actual_page_title}'"

        assert main_page.is_more_info_button_visible(), "Кнопка 'Подробнее' не отображается"
        assert main_page.is_more_info_button_clickable(), "Кнопка 'Подробнее' не кликабельна"

    # Проверки для раздела О нас

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

    # Проверки для раздела Услуги

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

    # Проверки для раздела Проекты

    @allure.title("Проверка перехода в раздел 'Проекты'")
    def test_transition_to_projects_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_projects_button()
        main_page.wait_for_url_contains("#cases")

        actual_url = driver.current_url
        expected_url = Urls.PROJECTS_BLOCK
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        assert main_page.is_first_task_visible(), "Первый проект не отображается"
        assert main_page.is_projects_title_visible(), "Заголовок 'Проекты' не отображается на экране 1920x1080"

    @allure.title("Проверка открытия всплывающего окна первого проекта")
    def test_first_task_popup_opens(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_projects_button()
        main_page.wait_for_url_contains("#cases")
        main_page.click_more_details_first_task()

        assert main_page.is_first_task_popup_visible(), "Всплывающее окно первого проекта не открылось"

    @allure.title("Проверка закрытия всплывающего окна первого проекта")
    def test_first_task_popup_closes(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_projects_button()
        main_page.wait_for_url_contains("#cases")
        main_page.click_more_details_first_task()

        assert main_page.is_first_task_popup_visible(), "Всплывающее окно не открылось"

        main_page.close_first_task_popup()

        assert main_page.is_first_task_popup_not_visible(), "Всплывающее окно первого проекта не закрылось"

    @allure.title("Проверка переключения слайдов проектов кнопкой 'Вперед'")
    def test_projects_slider_forward(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_projects_button()
        main_page.wait_for_url_contains("#cases")

        assert main_page.is_first_task_visible(), "Первый проект не отображается"

        main_page.click_forward_button()
        assert main_page.is_second_task_visible(), "Второй проект не отображается после переключения"

        main_page.click_forward_button()
        assert main_page.is_third_task_visible(), "Третий проект не отображается после переключения"

    @allure.title("Проверка переключения слайдов проектов кнопкой 'Назад'")
    def test_projects_slider_backward(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_projects_button()
        main_page.wait_for_url_contains("#cases")

        main_page.click_back_button()
        assert main_page.is_third_task_visible(), "Третий проект не отображается"

        main_page.click_back_button()
        assert main_page.is_second_task_visible(), "Второй проект не отображается после возврата"

    # Проверки для раздела Отзывы

    @allure.title("Проверка перехода в раздел 'Отзывы'")
    def test_transition_to_reviews_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_reviews_button()
        main_page.wait_for_url_contains("#Reviews")

        actual_url = driver.current_url
        expected_url = Urls.REVIEWS_BLOCK
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        actual_title = main_page.get_reviews_title()
        expected_title = "ОТЗЫВЫ КЛИЕНТОВ"
        assert actual_title == expected_title, f"Ожидался заголовок '{expected_title}', а получен '{actual_title}'"

        assert main_page.is_first_review_visible(), "Первый по дефолту отзыв компании 'SkillStaff' не отображается"

    @allure.title("Проверка переключения отзывов кнопкой 'Вперед'")
    def test_reviews_slider_forward(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_reviews_button()
        main_page.wait_for_url_contains("#Reviews")

        assert main_page.is_first_review_visible(), "Первый отзыв не отображается"

        main_page.click_forward_review_button()
        assert main_page.is_second_review_visible(), "Второй отзыв не отображается после переключения"

        main_page.click_forward_review_button()
        assert main_page.is_third_review_visible(), "Третий отзыв не отображается после переключения"

    @allure.title("Проверка переключения отзывов кнопкой 'Назад'")
    def test_reviews_slider_backward(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_reviews_button()
        main_page.wait_for_url_contains("#Reviews")

        main_page.click_previous_review_button()
        assert main_page.is_third_review_visible(), "Третий отзыв не отображается"

        main_page.click_previous_review_button()
        assert main_page.is_second_review_visible(), "Второй отзыв не отображается"

    # Проверки для раздела Контакты

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

    # Проверки для внешних ссылок раздела Контакты

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

    # Проверки для формы заявки

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

    # Проверки для раздела Специалисты

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

    # Проверки для раздела "Подберем для вас"

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

        main_page.scroll_to_select_it_for_you_section()
        main_page.click_submit_request_for_consult_button()

        assert main_page.is_popup_any_other_question_visible(), \
            "Всплывающее окно 'Остались вопросы?' не открылось"

    @allure.title("Проверка заполнения и отправки формы 'Остались вопросы?'")
    def test_submit_any_other_question_form(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.scroll_to_select_it_for_you_section()
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

        main_page.scroll_to_select_it_for_you_section()
        main_page.click_submit_request_for_consult_button()

        assert main_page.is_popup_any_other_question_visible(), \
            "Всплывающее окно 'Остались вопросы?' не открылось"

        main_page.close_popup_any_other_question()

        assert main_page.is_popup_any_other_question_closed(), \
            "Всплывающее окно 'Остались вопросы?' не закрылось"
