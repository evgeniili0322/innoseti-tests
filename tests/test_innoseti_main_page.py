from innoseti_tests.pages.main_page import MainPage

main_page = MainPage()


def test_assert_elements_texts():
    main_page.open()

    main_page.assert_banner_text()
    main_page.assert_info_text()
    main_page.assert_partners_text()


def test_go_to_products_page():
    main_page.open()

    main_page.go_to_products_page()

    main_page.assert_opened_product_page()


def test_go_to_work_us_page():
    main_page.open()

    main_page.go_to_work_with_us_page()

    main_page.assert_opened_work_with_us_page()


def test_go_to_news_page():
    main_page.open()

    main_page.go_to_news_page()

    main_page.assert_opened_news_page()
