import allure
from pages.main_page import MainPage
from urls import Urls

class TestReviewsSection:

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
