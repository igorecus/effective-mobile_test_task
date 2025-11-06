import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from urls import Urls

class MainPage(BasePage):

    # Методы для главной страницы

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.get(Urls.MAIN_PAGE)

    @allure.step("Получить название логотипа страницы")
    def get_page_logo(self):
        text = self.get_text_on_element(MainPageLocators.LOGO)
        return text

    @allure.step("Проверить наличие заголовка страницы")
    def is_page_title_visible(self):
        return self.wait_for_element(MainPageLocators.MAIN_TITLE)

    @allure.step("Проверить наличие кнопки 'Подробнее'")
    def is_more_info_button_visible(self):
        return self.wait_for_element(MainPageLocators.ABOUT_US_DESCRIPTION)

    @allure.step("Проверить кликабельность кнопки 'Подробнее'")
    def is_more_info_button_clickable(self):
        return self.wait_for_element_to_be_clickable(MainPageLocators.MORE_INFO_BUTTON)

    # Методы для раздела "О нас"

    @allure.step("Кликаем по кнопке «О нас» в Хедере")
    def click_about_us_button(self):
        self.click_on_element(MainPageLocators.ABOUT_US)

    @allure.step("Получить текст заголовка 'О нас'")
    def get_about_us_title(self):
        return self.get_text_on_element(MainPageLocators.ABOUT_US_TITLE)

    @allure.step("Проверить видимость описания 'О нас'")
    def is_about_us_description_visible(self):
        return self.wait_for_element(MainPageLocators.ABOUT_US_DESCRIPTION)

    @allure.step("Проверить видимость блока 'Наша цель'")
    def is_our_goal_visible(self):
        return self.wait_for_element(MainPageLocators.OUR_GOAL)

    # Методы для раздела "Почему мы"

    @allure.step("Скроллим до раздела 'Почему мы'")
    def scroll_to_why_we_section(self):
        self.scroll_to_element(MainPageLocators.WHY_WE_TITLE)

    @allure.step("Получить текст заголовка 'Почему мы'")
    def get_why_we_title(self):
        return self.get_text_on_element(MainPageLocators.WHY_WE_TITLE)

    @allure.step("Проверить видимость заголовка 'Почему мы'")
    def is_why_we_title_visible(self):
        return self.wait_for_element(MainPageLocators.WHY_WE_TITLE)

    @allure.step("Проверить видимость карточки 1 'Сокращение рисков найма'")
    def is_card_1_visible(self):
        return self.wait_for_element(MainPageLocators.CARD_1)

    @allure.step("Проверить видимость карточки 2 'Широкий выбор специалистов'")
    def is_card_2_visible(self):
        return self.wait_for_element(MainPageLocators.CARD_2)

    @allure.step("Проверить видимость карточки 3 'Эффективное распределение ресурсов'")
    def is_card_3_visible(self):
        return self.wait_for_element(MainPageLocators.CARD_3)

    @allure.step("Проверить видимость карточки 4 'Быстрое привлечение специалистов'")
    def is_card_4_visible(self):
        return self.wait_for_element(MainPageLocators.CARD_4)

    @allure.step("Проверить видимость карточки 5 'Отсутствие бумажной волокиты'")
    def is_card_5_visible(self):
        return self.wait_for_element(MainPageLocators.CARD_5)

    @allure.step("Скроллим до кнопки 'Оставить заявку на сотрудничество'")
    def scroll_to_application_form_link(self):
        self.scroll_to_element(MainPageLocators.LINK_TO_THE_APPLICATION_FORM)

    @allure.step("Проверить видимость кнопки 'Оставить заявку на сотрудничество'")
    def is_link_to_application_form_visible(self):
        return self.wait_for_element(MainPageLocators.LINK_TO_THE_APPLICATION_FORM)

    @allure.step("Кликнуть по кнопке 'Оставить заявку на сотрудничество'")
    def click_link_to_application_form(self):
        self.click_on_element(MainPageLocators.LINK_TO_THE_APPLICATION_FORM)

    # Методы для раздела "Услуги"

    @allure.step("Кликаем по кнопке «Услуги» в Хедере")
    def click_services_button(self):
        self.click_on_element(MainPageLocators.SERVICES)

    @allure.step("Получить текст заголовка раздела 'Услуги'")
    def get_services_title(self):
        return self.get_text_on_element(MainPageLocators.SERVICES_TITLE)

    @allure.step("Проверить видимость текста 'Разработка мобильных приложений'")
    def is_development_text_visible(self):
        return self.wait_for_element(MainPageLocators.DEVELOPMENT_TEXT)

    @allure.step("Проверить видимость текста 'Аутстаффинг IT-персонала'")
    def is_outstaffing_text_visible(self):
        return self.wait_for_element(MainPageLocators.OUTSTAFFING_TEXT)

    @allure.step("Проверить видимость текста 'Консалтинг'")
    def is_consulting_text_visible(self):
        return self.wait_for_element(MainPageLocators.CONSULTING_TEXT)

    # Методы для раздела "Проекты"

    @allure.step("Кликаем по кнопке «Проекты» в Хедере")
    def click_projects_button(self):
        self.click_on_element(MainPageLocators.PROJECTS)

    @allure.step("Проверить видимость заголовка 'Проекты'")
    def is_projects_title_visible(self):
        try:
            element = self.wait_for_element(MainPageLocators.PROJECTS_TITLE, timeout=5)
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить видимость первого проекта")
    def is_first_task_visible(self):
        return self.wait_for_element(MainPageLocators.FIRST_TASK)

    @allure.step("Проверить видимость второго проекта")
    def is_second_task_visible(self):
        return self.wait_for_element(MainPageLocators.SECOND_TASK)

    @allure.step("Проверить видимость третьего проекта")
    def is_third_task_visible(self):
        return self.wait_for_element(MainPageLocators.THIRD_TASK)

    @allure.step("Кликнуть по кнопке 'Подробнее' первого проекта")
    def click_more_details_first_task(self):
        self.click_on_element(MainPageLocators.MORE_DETAILS_BUTTON_FIRST_TASK)

    @allure.step("Кликнуть по кнопке 'Подробнее' второго проекта")
    def click_more_details_second_task(self):
        self.click_on_element(MainPageLocators.MORE_DETAILS_BUTTON_SECOND_TASK)

    @allure.step("Кликнуть по кнопке 'Подробнее' третьего проекта")
    def click_more_details_third_task(self):
        self.click_on_element(MainPageLocators.MORE_DETAILS_BUTTON_THIRD_TASK)

    @allure.step("Проверить видимость всплывающего окна первого проекта")
    def is_first_task_popup_visible(self):
        return self.wait_for_element(MainPageLocators.FIRST_TASK_POPUP)

    @allure.step("Проверить видимость всплывающего окна второго проекта")
    def is_second_task_popup_visible(self):
        return self.wait_for_element(MainPageLocators.SECOND_TASK_POPUP)

    @allure.step("Проверить видимость всплывающего окна третьего проекта")
    def is_third_task_popup_visible(self):
        return self.wait_for_element(MainPageLocators.THIRD_TASK_POPUP)

    @allure.step("Закрыть всплывающее окно первого проекта")
    def close_first_task_popup(self):
        self.click_on_element(MainPageLocators.FIRST_TASK_CLOSE_BUTTON)

    @allure.step("Закрыть всплывающее окно второго проекта")
    def close_second_task_popup(self):
        self.click_on_element(MainPageLocators.SECOND_TASK_CLOSE_BUTTON)

    @allure.step("Закрыть всплывающее окно третьего проекта")
    def close_third_task_popup(self):
        self.click_on_element(MainPageLocators.THIRD_TASK_CLOSE_BUTTON)

    @allure.step("Проверить закрытие всплывающего окна первого проекта")
    def is_first_task_popup_not_visible(self):
        return self.wait_for_element_to_disappear(MainPageLocators.FIRST_TASK_POPUP)

    @allure.step("Проверить закрытие всплывающего окна второго проекта")
    def is_second_task_popup_not_visible(self):
        return self.wait_for_element_to_disappear(MainPageLocators.SECOND_TASK_POPUP)

    @allure.step("Проверить закрытие всплывающего окна третьего проекта")
    def is_third_task_popup_not_visible(self):
        return self.wait_for_element_to_disappear(MainPageLocators.THIRD_TASK_POPUP)

    @allure.step("Кликнуть по кнопке 'Следующий слайд'")
    def click_forward_button(self):
        self.click_on_element(MainPageLocators.FORWARD_BUTTON)

    @allure.step("Кликнуть по кнопке 'Предыдущий слайд'")
    def click_back_button(self):
        self.click_on_element(MainPageLocators.BACK_BUTTON)

    # Методы для раздела "Отзывы"

    @allure.step("Кликаем по кнопке «Отзывы» в Хедере")
    def click_reviews_button(self):
        self.click_on_element(MainPageLocators.REVIEWS)

    @allure.step("Получить текст заголовка 'Отзывы клиентов'")
    def get_reviews_title(self):
        return self.get_text_on_element(MainPageLocators.CUSTOMER_REVIEWS_TITLE)

    @allure.step("Проверить видимость первого отзыва")
    def is_first_review_visible(self):
        return self.wait_for_element(MainPageLocators.FIRST_REVIEW)

    @allure.step("Проверить видимость второго отзыва")
    def is_second_review_visible(self):
        return self.wait_for_element(MainPageLocators.SECOND_REVIEW)

    @allure.step("Проверить видимость третьего отзыва")
    def is_third_review_visible(self):
        return self.wait_for_element(MainPageLocators.THIRD_REVIEW)

    @allure.step("Кликнуть по кнопке 'Следующий отзыв'")
    def click_forward_review_button(self):
        self.click_on_element(MainPageLocators.FORWARD_REVIEW_BUTTON)

    @allure.step("Кликнуть по кнопке 'Предыдущий слайд'")
    def click_previous_review_button(self):
        self.click_on_element(MainPageLocators.PREVIOUS_REVIEW_BUTTON)

    # Методы для раздела "Контакты"

    @allure.step("Кликаем по кнопке «Контакты» в Хедере")
    def click_contacts_button(self):
        self.click_on_element(MainPageLocators.CONTACTS)

    @allure.step("Получить текст заголовка 'Контакты'")
    def get_contacts_title(self):
        return self.get_text_on_element(MainPageLocators.CONTACTS_SECTION_TITLE)

    @allure.step("Получить текст призыва к действию 'Оставьте заявку...'")
    def get_call_to_action_text(self):
        return self.get_text_on_element(MainPageLocators.CALL_TO_ACTION_TEXT)

    @allure.step("Проверить видимость формы заявки на консультацию ")
    def is_contact_form_visible(self):
        return self.wait_for_element(MainPageLocators.CONTACT_FORM)

    @allure.step("Проверить видимость ссылки на IT поддержку")
    def is_it_support_link_visible(self):
        return self.wait_for_element(MainPageLocators.IT_SUPPORT_LINK)

    @allure.step("Проверить видимость ссылки на Telegram")
    def is_telegram_link_visible(self):
        return self.wait_for_element(MainPageLocators.TELEGRAM_LINK)

    @allure.step("Проверить видимость ссылки на Email")
    def is_email_link_visible(self):
        return self.wait_for_element(MainPageLocators.EMAIL_LINK)

    @allure.step("Проверить видимость ссылки на Политику конфиденциальности")
    def is_privacy_link_visible(self):
        return self.wait_for_element(MainPageLocators.PRIVACY_LINK)

    @allure.step("Получить href ссылки на IT поддержку")
    def get_it_support_link_href(self):
        return self.get_element_href(MainPageLocators.IT_SUPPORT_LINK)

    @allure.step("Получить href ссылки на Telegram")
    def get_telegram_link_href(self):
        return self.get_element_href(MainPageLocators.TELEGRAM_LINK)

    @allure.step("Получить href ссылки на Email")
    def get_email_link_href(self):
        return self.get_element_href(MainPageLocators.EMAIL_LINK)

    @allure.step("Получить href ссылки на Политику конфиденциальности")
    def get_privacy_link_href(self):
        return self.get_element_href(MainPageLocators.PRIVACY_LINK)

    # Методы для формы заявки

    @allure.step("Заполнить поле 'Имя'")
    def fill_first_name_field(self, name):
        self.send_keys_to_input(MainPageLocators.FILL_FIRST_NAME_FIELD, name)

    @allure.step("Заполнить поле 'Телефон'")
    def fill_phone_field(self, phone):
        self.send_keys_to_input(MainPageLocators.FILL_PHONE_FIELD, phone)

    @allure.step("Заполнить поле 'Telegram'")
    def fill_telegram_field(self, telegram):
        self.send_keys_to_input(MainPageLocators.FILL_YOUR_TELEGRAM_FIELD, telegram)

    @allure.step("Заполнить поле 'Дополнительная информация'")
    def fill_additional_info_field(self, info):
        self.send_keys_to_input(MainPageLocators.FILL_ADD_INFO_AREA, info)

    @allure.step("Кликнуть по кнопке 'Отправить'")
    def click_send_button(self):
        self.click_on_element(MainPageLocators.SEND_BUTTON)

    @allure.step("Проверить отображение сообщения об успешной отправке")
    def is_success_message_visible(self):
        return self.wait_for_element(MainPageLocators.SUCCESS_MESSAGE)

    # Методы для раздела "Специалисты"

    @allure.step("Кликаем по кнопке «Выбрать специалиста» в Хедере")
    def click_choose_a_super_hero_button(self):
        self.click_on_element(MainPageLocators.CHOOSE_A_SUPER_HERO_BUTTON)

    @allure.step("Получить текст заголовка 'Наш стек'")
    def get_our_stack_title(self):
        return self.get_text_on_element(MainPageLocators.OUR_STACK_TITLE)

    @allure.step("Проверить видимость заголовка 'Android (нативная разработка)'")
    def is_android_dev_title_visible(self):
        return self.wait_for_element(MainPageLocators.ANDROID_TITLE)

    @allure.step("Проверить видимость заголовка 'iOS (нативная разработка)'")
    def is_ios_dev_title_visible(self):
        return self.wait_for_element(MainPageLocators.IOS_TITLE)

    @allure.step("Проверить видимость заголовка 'Flutter (кросплатформенная разработка)'")
    def is_flutter_dev_title_visible(self):
        return self.wait_for_element(MainPageLocators.FLUTTER_TITLE)

    # Методы для раздела "Подберем для вас"

    @allure.step("Скроллим до раздела 'Подберем для вас'")
    def scroll_to_select_it_for_you_section(self):
        self.scroll_to_element_advance(MainPageLocators.SELECT_IT_FOR_YOU_TITLE)

    @allure.step("Получить текст заголовка 'Подберем для вас'")
    def get_select_it_for_you_title(self):
        return self.get_text_on_element(MainPageLocators.SELECT_IT_FOR_YOU_TITLE)

    @allure.step("Проверить видимость заголовка 'Подберем для вас'")
    def is_select_it_for_you_title_visible(self):
        return self.wait_for_element(MainPageLocators.SELECT_IT_FOR_YOU_TITLE)

    @allure.step("Проверить видимость карточки 'Mobile-разработчик'")
    def is_mobile_dev_card_visible(self):
        self.scroll_to_element(MainPageLocators.DEVELOPMENT_MOBILE_DEV)
        return self.wait_for_element(MainPageLocators.DEVELOPMENT_MOBILE_DEV)

    @allure.step("Проверить видимость карточки 'Бизнес-аналитик'")
    def is_business_analyst_card_visible(self):
        self.scroll_to_element(MainPageLocators.ANALYTICS_BIZ_AN)
        return self.wait_for_element(MainPageLocators.ANALYTICS_BIZ_AN)

    @allure.step("Проверить видимость карточки 'QA автоматизатор'")
    def is_qa_auto_card_visible(self):
        self.scroll_to_element(MainPageLocators.QA_AUTO_CARD)
        return self.wait_for_element(MainPageLocators.QA_AUTO_CARD)

    @allure.step("Проверить видимость карточки 'PHP-разработчик'")
    def is_php_dev_card_visible(self):
        self.scroll_to_element(MainPageLocators.DEVELOPMENT_PHP)
        return self.wait_for_element(MainPageLocators.DEVELOPMENT_PHP)

    @allure.step("Проверить видимость карточки '1С-аналитик'")
    def is_1c_analyst_card_visible(self):
        self.scroll_to_element(MainPageLocators.ANALYTICS_1C)
        return self.wait_for_element(MainPageLocators.ANALYTICS_1C)

    @allure.step("Проверить видимость кнопки 'Оставить заявку на консультацию'")
    def is_apply_button_visible(self):
        self.scroll_to_element(MainPageLocators.SUBMIT_A_REQUEST_FOR_CONSULT_BUTTON)
        return self.wait_for_element(MainPageLocators.SUBMIT_A_REQUEST_FOR_CONSULT_BUTTON)

    @allure.step("Скроллим до кнопки 'Оставить заявку на консультацию'")
    def scroll_to_submit_request_for_consult_button(self):
        self.scroll_to_element_advance(MainPageLocators.SUBMIT_A_REQUEST_FOR_CONSULT_BUTTON)

    @allure.step("Кликнуть по кнопке 'Оставить заявку на консультацию'")
    def click_submit_request_for_consult_button(self):
        self.click_on_element(MainPageLocators.SUBMIT_A_REQUEST_FOR_CONSULT_BUTTON)

    # Методы для всплывающего окна "Остались вопросы?"

    @allure.step("Проверить видимость всплывающего окна 'Остались вопросы?'")
    def is_popup_any_other_question_visible(self):
        return self.wait_for_element(MainPageLocators.POPUP_WINDOW_ANY_OTHER_QUESTION)

    @allure.step("Заполнить поле 'Имя' в попапе")
    def fill_popup_first_name_field(self, name):
        self.send_keys_to_input(MainPageLocators.FIRST_NAME_FIELD, name)

    @allure.step("Заполнить поле 'Ваш Telegram' в попапе")
    def fill_popup_telegram_field(self, telegram):
        self.send_keys_to_input(MainPageLocators.YOUR_TELEGRAM_FIELD, telegram)

    @allure.step("Кликнуть по кнопке 'Отправить' в попапе")
    def click_popup_submit_button(self):
        self.click_on_element(MainPageLocators.SUBMIT_BUTTON)

    @allure.step("Проверить отображение сообщения об успешной отправке в попапе")
    def is_popup_success_message_visible(self):
        return self.wait_for_element(MainPageLocators.SUCCESSFULLY_SENT_DATA_WINDOW)

    @allure.step("Закрыть всплывающее окно 'Остались вопросы?'")
    def close_popup_any_other_question(self):
        self.click_on_element(MainPageLocators.CLOSE_POPUP_BUTTON)

    @allure.step("Проверить закрытие всплывающего окна 'Остались вопросы?'")
    def is_popup_any_other_question_closed(self):
        return self.wait_for_element_to_disappear(MainPageLocators.POPUP_WINDOW_ANY_OTHER_QUESTION)

    # Методы для раздела "Футер"

    @allure.step("Скроллим до раздела Футер")
    def scroll_to_footer_section(self):
        self.scroll_to_element(MainPageLocators.FOOTER_TITLE)

    @allure.step("Проверить видимость логотипа футера")
    def is_footer_title_visible(self):
        return self.wait_for_element(MainPageLocators.FOOTER_TITLE)

    @allure.step("Проверить видимость юридической информации компании")
    def is_company_info_visible(self):
        return self.wait_for_element(MainPageLocators.COMPANY_INFO)

    @allure.step("Проверить видимость копирайта")
    def is_copyright_visible(self):
        return self.wait_for_element(MainPageLocators.COPYRIGHT)

    @allure.step("Проверить видимость ссылки на Политику конфиденциальности в футере")
    def is_footer_privacy_link_visible(self):
        return self.wait_for_element(MainPageLocators.FOOTER_PRIVATE_POLICY_LINK)

    @allure.step("Кликнуть по логотипу футера")
    def click_footer_title(self):
        self.click_on_element(MainPageLocators.FOOTER_TITLE)

    @allure.step("Получить href ссылки на Политику конфиденциальности в футере")
    def get_footer_privacy_link_href(self):
        return self.get_element_href(MainPageLocators.FOOTER_PRIVATE_POLICY_LINK)
