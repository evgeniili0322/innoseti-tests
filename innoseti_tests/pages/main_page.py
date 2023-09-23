import allure

from selene import browser, have, be


class MainPage:
    @allure.step('Open main page')
    def open(self):
        browser.open('')

    @allure.step('Assert banner text')
    def assert_banner_text(self):
        browser.element('[field="tn_text_1679499443035"]').should(have.exact_text('Создаём инфраструктурные сетевые '
                                                                                  'решения для крупного бизнеса в '
                                                                                  'сфере страхования логистики и '
                                                                                  'медицины, специализируемся на '
                                                                                  'работе со сложными технологиями, '
                                                                                  'в том числе блокчейн и нейронные '
                                                                                  'сети.'))

    @allure.step('Assert info text')
    def assert_info_text(self):
        browser.all('#rec571160648 .tn-atom').odd.should(have.exact_texts(
            'Нами создана крупнейшая транзакционная сеть на блокчейне в России — более 100 транзакций в секунду',
            'Мы — ИТ-компания, аккредитованная Минцифры России',
            'С июля 2018 г. — резидент особой экономической зоны в Калининградской области',
            'Решения компании зарегистрированы в реестре отечественного ПО'
        ))

    @allure.step('Assert partners text')
    def assert_partners_text(self):
        browser.all('#rec571157876 [data-elem-type="text"]').should(have.exact_texts(
            'Партнёры',
            'С нами работают 8 из 15 крупнейших страховых компаний России'
        ))

    @allure.step('Go to products page')
    def go_to_products_page(self):
        browser.element('[data-menu-item-number="2"]').click()

    @allure.step('Assert opened products page')
    def assert_opened_products_page(self):
        browser.element('[field=title]').should(be.visible).should(have.exact_text('Продукты'))

    @allure.step('Go to work with us page')
    def go_to_work_with_us_page(self):
        browser.element('[data-menu-item-number="3"]').click()

    @allure.step('Assert opened work with us page')
    def assert_opened_work_with_us_page(self):
        (browser.element('[field=tn_text_1688389796413]').should(be.visible).
         should(have.exact_text('Привет!\nМы —«Инносети»')))

    @allure.step('Go to news page')
    def go_to_news_page(self):
        browser.element('[data-menu-item-number="4"]').click()

    @allure.step('Assert opened news page')
    def assert_opened_news_page(self):
        browser.element('[field=title]').should(be.visible).should(have.exact_text('Новости'))

    @allure.step('Go to article page')
    def go_to_article_page(self):
        browser.all('.js-feed-post').first.click()

    @allure.step('Assert opened article page')
    def assert_opened_article_page(self):
        browser.element('.t758 .t-container').should(be.visible).should(have.text('Главная\n→\nНовости'))
