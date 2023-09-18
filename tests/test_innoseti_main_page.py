import allure

from allure_commons.types import Severity
from innoseti_tests.pages.main_page import MainPage

main_page = MainPage()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Assert elements texts')
@allure.link('https://innoseti.ru/')
def test_assert_elements_texts():
    main_page.open()

    main_page.assert_banner_text()
    main_page.assert_info_text()
    main_page.assert_partners_text()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Go to products page')
@allure.link('https://innoseti.ru/')
def test_go_to_products_page():
    main_page.open()

    main_page.go_to_products_page()

    main_page.assert_opened_products_page()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Go to work with us page')
@allure.link('https://innoseti.ru/')
def test_go_to_work_us_page():
    main_page.open()

    main_page.go_to_work_with_us_page()

    main_page.assert_opened_work_with_us_page()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Go to news page')
@allure.link('https://innoseti.ru/')
def test_go_to_news_page():
    main_page.open()

    main_page.go_to_news_page()

    main_page.assert_opened_news_page()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Go to article page')
@allure.link('https://innoseti.ru/')
def test_open_article():
    main_page.open()

    main_page.go_to_article_page()

    main_page.assert_opened_article_page()
