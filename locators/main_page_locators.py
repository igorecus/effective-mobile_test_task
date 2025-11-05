from selenium.webdriver.common.by import By


class MainPageLocators:
    # Header
    LOGO = (By.XPATH, "//a[text()='Effective Mobile']")
    ABOUT_US = (By.XPATH, "//a[text()='[ О нас ]']")
    SERVICES = (By.XPATH, "//a[text()='[ Услуги ]']")
    PROJECTS = (By.XPATH, "//a[text()='[ Проекты ]']")
    REVIEWS = (By.XPATH, "//a[text()='[ Отзывы ]']")
    CONTACTS = (By.XPATH, "//span[text()='[ Контакты ]']")
    CHOOSE_A_SUPER_HERO_BUTTON = (By.XPATH, "//a[text()='Выбрать специалиста']")

    # Hero section
    MAIN_TITLE = (By.XPATH, "//h1[contains(., 'Разработка') and contains(., 'мобильных приложений')]")
    MORE_INFO_BUTTON = (By.XPATH, "//a[text()='Подробнее']")

    # About us section
    ABOUT_US_TITLE = (By.XPATH, "//div[text()='О нас']")
    ABOUT_US_DESCRIPTION = (
    By.XPATH, "//div[@field='tn_text_1680508197689' and contains(., 'Effective Mobile — это команда экспертов')]")
    OUR_GOAL = (By.XPATH, "//div[@field='tn_text_1680508197711']")

    # Why we section
    WHY_WE_TITLE = (By.XPATH, "//div[text()='почему мы']")
    CARD_1 = (By.XPATH, "//div[@data-elem-id='1680508756753']/div[text()='сокращение рисков найма']")
    CARD_2 = (By.XPATH, "//div[@data-elem-id='1680509635346']/div[text()='широкий выбор специалистов']")
    CARD_3 = (By.XPATH, "//div[@data-elem-id='1680509693081']/div[text()='Эффективное распределение ресурсов']")
    CARD_4 = (By.XPATH, "//div[@data-elem-id='1680509729267']/div[text()='Быстрое привлечение специалистов']")
    CARD_5 = (By.XPATH,
    "//div[@data-elem-id='1680509733582']/div[contains(., 'отсутствие') and contains(., 'бумажной волокиты')]")
    LINK_TO_THE_APPLICATION_FORM = (By.XPATH, "//div[@id='sbs-572374517-1680509731311']")

    # Services section
    SERVICES_TITLE = (By.XPATH, "//div[text()='услуги']")
    DEVELOPMENT_TEXT = (By.XPATH, "//h2[contains(., 'Разработка') and contains(., 'мобильных приложений')]")
    OUTSTAFFING_TEXT = (By.XPATH, "//h2[contains(., 'АУТСТАФФИНГ ') and contains(., 'IT-персонала и специалистов')]")
    CONSULTING_TEXT = (By.XPATH, "//h2[contains(., 'Консалтинг') and contains(., 'в сфере мобильных разработок')]")

    # Projects section
    PROJECTS_TITLE = (By.XPATH, "//div[text()='проекты']")
    FIRST_TASK = (By.XPATH, "(//div[@field='li_title__1496797390759'])[1]")
    MORE_DETAILS_BUTTON_FIRST_TASK = (By.XPATH, "(//a[@data-lid='1496797390759'])[1]")
    FIRST_TASK_POPUP = (By.XPATH, "(//img[@class='t390__img t-img loaded'])[1]")
    FIRST_TASK_CLOSE_BUTTON = (By.XPATH, "//div[@id='rec572844014']//button[@aria-label='Закрыть диалоговое окно']")

    SECOND_TASK = (By.XPATH, "(//div[@field='li_title__1496797396352'])[1]")
    MORE_DETAILS_BUTTON_SECOND_TASK = (By.XPATH, "(//a[@data-lid='1496797396352'])[1]")
    SECOND_TASK_POPUP = (By.XPATH, "(//img[@class='t390__img t-img loaded'])[1]")
    SECOND_TASK_CLOSE_BUTTON = (By.XPATH, "//div[@id='rec572851038']//button[@aria-label='Закрыть диалоговое окно']")

    THIRD_TASK = (By.XPATH, "(//div[@field='li_title__1680581683689'])[1]")
    MORE_DETAILS_BUTTON_THIRD_TASK = (By.XPATH, "(//a[@data-lid='1496797390759'])[1]")
    THIRD_TASK_POPUP = (By.XPATH, "(//img[@class='t390__img t-img loaded'])[1]")
    THIRD_TASK_CLOSE_BUTTON = (By.XPATH, "//div[@id='rec572851409']//button[@aria-label='Закрыть диалоговое окно']")

    FORWARD_BUTTON = (By.XPATH, "//button[@aria-label='Следующий слайд']")
    BACK_BUTTON = (By.XPATH, "//button[@aria-label='Предыдущий слайд']")

    # Our Stack section
    OUR_STACK_TITLE = (By.XPATH, "//span[text()='Наш стек']")
    ANDROID_TEXT = (By.XPATH, "//span[text()='Android (нативная разработка)']")
    IOS_TEXT = (By.XPATH, "//span[text()='iOS (нативная разработка)']")
    FLUTTER_TEXT = (By.XPATH, "//span[text()='Flutter (кросплатформенная разработка)']")

    # Select it for you section
    SELECT_IT_FOR_YOU_TITLE = (By.XPATH, "//div[@data-elem-id='1680514720242']")
    DEVELOPMENT_MOBILE_DEV = (By.XPATH, "//div[@id='sbs-572441941-1748203600215']")
    ANALYTICS_BIZ_AN = (By.XPATH, "//div[@id='sbs-572441941-1680514742797']")
    QA_AUTO_CARD = (By.XPATH, "//div[@id='sbs-572441941-1748204146196']")
    DEVELOPMENT_PHP = (By.XPATH, "//div[@id='sbs-572441941-1748204593629']")
    ANALYTICS_1C = (By.XPATH, "//div[@id='sbs-572441941-1748205943187']")

    SUBMIT_A_REQUEST_FOR_CONSULT_BUTTON = (By.XPATH, "//div[@id='sbs-572441941-1680515472080']")
    POPUP_WINDOW_ANY_OTHER_QUESTION = (By.XPATH, "//div[contains(@class, 't-popup_show')]")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='input_1495810354468']")
    YOUR_TELEGRAM_FIELD = (By.XPATH, "//input[@id='input_1495810359387']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@id='input_1495810359387']/following::button[@type='submit'][1]")
    CLOSE_POPUP_BUTTON = (By.XPATH,
    "//div[contains(@class, 't-popup_show')]//button[@aria-label='Закрыть диалоговое окно']")
    SUCCESSFULLY_SENT_DATA_WINDOW = (By.XPATH, "//div[@id='tildaformsuccesspopuptext-new']")

    # Customer reviews section
    CUSTOMER_REVIEWS_TITLE = (By.XPATH, "//strong[text()='ОТЗЫВЫ КЛИЕНТОВ']")
    FIRST_REVIEW = (By.XPATH, "(//div[@data-slide-index='1'])[2]")
    SECOND_REVIEW = (By.XPATH, "(//div[@data-slide-index='2'])[2]")
    THIRD_REVIEW = (By.XPATH, "(//div[@data-slide-index='3'])[2]")

    FORWARD_REVIEW_BUTTON = (By.XPATH, "(//button[@aria-label='Следующий слайд'])[2]")
    PREVIOUS_REVIEW_BUTTON = (By.XPATH, "(//button[@aria-label='Предыдущий слайд'])[2]")

    # Contacts section
    CONTACTS_SECTION_TITLE = (By.XPATH, "//div[text()='контакты']")
    CALL_TO_ACTION_TEXT = (By.XPATH, "//div[@field='tn_text_1680515874720']")
    CONTACT_FORM = (By.XPATH, "//div[@data-elem-id='1680516551683']")

    FILL_FIRST_NAME_FIELD = (By.XPATH, "//input[@id='nm-1531306243545']")
    FILL_PHONE_FIELD = (By.XPATH, "//input[@id='input_1531306540094']")
    FILL_YOUR_TELEGRAM_FIELD = (By.XPATH, "//input[@id='in-1680516575724']")
    FILL_ADD_INFO_AREA = (By.XPATH, "//textarea[@id='ta-1680516600617']")
    SEND_BUTTON = (By.XPATH, "//textarea[@id='ta-1680516600617']/following::button[@type='submit'][1]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='tildaformsuccesspopuptext']")

    IT_SUPPORT_LINK = (By.XPATH, "//a[@href='https://t.me/assistant_em']")
    TELEGRAM_LINK = (By.XPATH, "//a[@href='https://t.me/krasnikova_d']")
    EMAIL_LINK = (By.XPATH, "//a[@href='mailto:dariia.krasnikova@effectivemobile.ru']")
    PRIVACY_LINK = (By.XPATH, "//a[@href='https://effective-mobile.ru/privacy']")

    PRIVATE_POLICY_HIGHLIGHTED_TEXT = (By.XPATH, "(//a[@href='https://effective-mobile.ru/privacy'])[1]")

    # FOOTER
    FOOTER_TITLE = (By.XPATH, "//div[@data-elem-id='1680517421264']")
    COMPANY_INFO = (By.XPATH, "//div[@field='tn_text_1680517517329']")
    FOOTER_PRIVATE_POLICY_LINK = (By.XPATH, "//a[@id='sbs-572471347-1680517572082']")
