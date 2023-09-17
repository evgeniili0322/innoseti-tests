import allure

from selene import browser, have


class MainPage:
    @allure.step('Open main page')
    def open(self):
        browser.open()

    @allure.step('Assert banner text')
    def assert_banner_text(self):
        browser.element('[data-artboard-recid="569655320"] .t396__filter').should(have.text(f'Инносети \nСоздаём '
                                                                                            f'инфраструктурные '
                                                                                            f'сетевые решения для '
                                                                                            f'крупного бизнеса в '
                                                                                            f'сфере страхования '
                                                                                            f'логистики и медицины, '
                                                                                            f'специализируемся на '
                                                                                            f'работе со сложными '
                                                                                            f'технологиями, '
                                                                                            f'в том числе блокчейн и '
                                                                                            f'нейронные сети. '))