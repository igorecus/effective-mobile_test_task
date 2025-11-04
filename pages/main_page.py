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
    def get_page_name(self):
        text = self.get_text_on_element(MainPageLocators.LOGO)
        return text

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




















    @allure.step("Кликаем по кнопке «Проекты» в Хедере")
    def click_projects_button(self):
        self.click_on_element(MainPageLocators.PROJECTS)

    @allure.step("Кликаем по кнопке «Отзывы» в Хедере")
    def click_reviews_button(self):
        self.click_on_element(MainPageLocators.REVIEWS)

    @allure.step("Кликаем по кнопке «Контакты» в Хедере")
    def click_contacts_button(self):
        self.click_on_element(MainPageLocators.CONTACTS)

    @allure.step("Кликаем по кнопке «Выбрать специалиста» в Хедере")
    def click_choose_a_super_hero_button(self):
        self.click_on_element(MainPageLocators.CHOOSE_A_SUPER_HERO_BUTTON)













    @allure.step("Получаем название страницы")
    def get_padffge_name(self):
        self.wait_for_attribute(MainPageLocators.LOGO, "textContent", "Соберите бургер")
        return self.find_element(MainPageLocators.ASSEMBLE_A_BURGER_TEXT).text


    @allure.step("Кликаем по кнопке «Конструктор»")
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)



    @allure.step("Кликаем по кнопке входа в личный кабинет")
    def click_personal_account_button(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликаем по кнопке «Лента Заказов»")
    def click_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликаем по ингридиенту - булке")
    def click_ingredient_bun_button(self):
        self.click_on_element(MainPageLocators.FLUORESCENT_ROLL_R2_D3)

    @allure.step("Кликаем по ингридиенту - соусу")
    def click_ingredient_sauce_button(self):
        self.click_on_element(MainPageLocators.SPICY_X_SAUCE)

    @allure.step("Скроллим до биокотлеты из марсианской Магнолии")
    def scroll_to_magnolia_patty(self):
        self.scroll_to_element(MainPageLocators.ORGANIC_MARTIAN_MAGNOLIA_PATTY)

    @allure.step("Кликаем по ингридиенту - начинке")
    def click_ingredient_topping_button(self):
        self.click_on_element(MainPageLocators.ORGANIC_MARTIAN_MAGNOLIA_PATTY)

    @allure.step("Закрываем всплывающее окно кликом по крестику")
    def click_close_up_ingredient_details_popup_button(self):
        self.click_on_element(MainPageLocators.CLOSE_POPUP_BUTTON)

    @allure.step("Получаем название окна с деталями ингридиента")
    def get_details_window_name(self):
        self.wait_for_attribute(MainPageLocators.DETAILS_WINDOW_TEXT, "textContent", "Детали ингредиента")
        return self.find_element(MainPageLocators.DETAILS_WINDOW_TEXT).text

    @allure.step("Ожидаем, что окно с деталями ингредиента закрылось")
    def wait_for_ingredient_modal_to_disappear(self):
        self.wait_for_element_hide(MainPageLocators.DETAILS_WINDOW_TEXT)

    @allure.step("Добавить ингридиент в заказ")
    def put_ingredient_into_basket(self):
        ingredient = self.wait_for_element(MainPageLocators.FLUORESCENT_ROLL_R2_D3)
        basket = self.wait_for_element(MainPageLocators.BASKET)
        self.drag_and_drop_element(ingredient, basket)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_count(self):
        text = self.get_text_on_element(MainPageLocators.COUNTER_FLUORESCENT_ROLL)
        return int(text)

    @allure.step("Кликаем по кнопке «Оформить заказ»")
    def click_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.get_text_on_element(MainPageLocators.ORDER_NUMBER_IN_MODAL)

    @allure.step("Получить текст сообщения 'Ваш заказ начали готовить'")
    def get_order_has_already_been_prepared_message_text(self):
        self.wait_for_element(MainPageLocators.ORDER_STARTED_TEXT)
        return self.get_text_on_element(MainPageLocators.ORDER_STARTED_TEXT)

    @allure.step("Кликаем по кнопке закрытия модального окна")
    def click_close_modal_window_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON, timeout=15)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)