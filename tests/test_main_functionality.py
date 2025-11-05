import allure
from pages.main_page import MainPage


class TestMainFunctionality:

    @allure.title("Проверка открытия страницы")
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
        assert actual_text == expected_text, f"Ожидался текст '{expected_page_title}', а получен '{actual_page_title}'"

        assert main_page.is_more_info_button_visible(), "Кнопка 'Подробнее' не отображается"
        assert main_page.is_more_info_button_clickable(), "Кнопка 'Подробнее' не кликабельна"

    @allure.title("Проверка перехода в раздел 'О нас'")
    def test_transition_to_about_us_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_about_us_button()
        main_page.wait_for_url_contains("#about")

        actual_url = driver.current_url
        expected_url = "https://effective-mobile.ru/#about"
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        assert main_page.is_about_us_description_visible(), "Описание раздела 'О нас' не отображается"
        assert main_page.is_our_goal_visible(), "Блок 'Наша цель' не отображается"

        actual_title = main_page.get_about_us_title()
        expected_title = "О нас"
        assert actual_title == expected_title, f"Ожидался заголовок '{expected_title}', а получен '{actual_title}'"

    @allure.title("Проверка перехода в раздел 'Услуги'")
    def test_transition_to_services_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_services_button()
        main_page.wait_for_url_contains("#moreinfo")

        actual_url = driver.current_url
        expected_url = "https://effective-mobile.ru/#moreinfo"
        assert actual_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{actual_url}'"

        actual_title = main_page.get_services_title()
        expected_title = "услуги"
        assert actual_title == expected_title, f"Ожидался заголовок '{expected_title}', а получен '{actual_title}'"

        assert main_page.is_development_text_visible(), "Текст 'Разработка мобильных приложений' не отображается"
        assert main_page.is_outstaffing_text_visible(), "Текст 'Аутстаффинг IT-персонала' не отображается"
        assert main_page.is_consulting_text_visible(), "Текст 'Консалтинг' не отображается"


    @allure.title("Проверка перехода в раздел 'Проекты'")
    def test_transition_to_projects_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_projects_button()
        main_page.wait_for_url_contains("#cases")

        actual_url = driver.current_url
        expected_url = "https://effective-mobile.ru/#cases"
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

    @allure.title("Проверка перехода в раздел 'Отзывы'")
    def test_transition_to_reviews_section(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_reviews_button()
        main_page.wait_for_url_contains("#Reviews")

        actual_url = driver.current_url
        expected_url = "https://effective-mobile.ru/#Reviews"
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