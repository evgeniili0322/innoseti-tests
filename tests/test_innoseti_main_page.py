from innoseti_tests.pages.main_page import MainPage

main_page = MainPage


def test_elements_texts():
    main_page.open()

    main_page.assert_banner_text()
