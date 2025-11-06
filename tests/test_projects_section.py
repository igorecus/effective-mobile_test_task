import allure
from pages.main_page import MainPage
from urls import Urls

@allure.feature("Главная страница")
@allure.story("Раздел 'Проекты'")
class TestProjectsSection:

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
