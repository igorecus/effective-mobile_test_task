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

