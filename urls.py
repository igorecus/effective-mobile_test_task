class Urls:
    # Главная страница
    BASE_URL = "https://effective-mobile.ru/"
    MAIN_PAGE = BASE_URL

    # Разделы Главной страницы
    ABOUT_COMPANY_BLOCK = f"{BASE_URL}#about"  # "О нас"
    SERVICES_BLOCK = f"{BASE_URL}#moreinfo"  # "Услуги"
    DETAILS_LINK = SERVICES_BLOCK # Ссылка "Подробнее" под заголовком страницы"
    PROJECTS_BLOCK = f"{BASE_URL}#cases"  # "Проекты"
    REVIEWS_BLOCK = f"{BASE_URL}#Reviews"  # "Отзывы"
    CONTACTS_BLOCK = f"{BASE_URL}#contacts"  # "Контакты"
    PRIVACY_POLICY = f"{BASE_URL}privacy"  # Политика конфиденциальности
    MAIN = f"{BASE_URL}#main"  # Главная

    # Внешние ссылки
    TELEGRAM_SUPPORT = "https://t.me/assistant_em"
    COFOUNDER_KRASNIKOVA_DARIIA_TELEGRAM_LINK = "https://t.me/krasnikova_d"
    EMAIL_SUPPORT = "mailto:dariia.krasnikova@effectivemobile.ru"
