# Проект по тестированию главной страницы сайта компании "ИННОСЕТИ"
> <a target="_blank" href="https://innoseti.ru/">Ссылка на cайт</a>

![This is an image](design/images/innoseti-main.png)

#### Список проверок, реализованных в автотестах
- [x] Проверка текстов элементов главной страницы
- [x] Проверка перехода на страницу "Продукты"
- [x] Проверка перехода на страницу "Работа у нас"
- [x] Проверка перехода на страницу "Новости"
- [x] Проверка открытия новостной статьи с главной страницы

## Технoлoгии и инструмeнты
<p align="center">
<a href="https://www.python.org/"><img src="design/icons/python.svg" width="50" height="50"  alt="Python" title="Python"/></a>
<a href="https://docs.pytest.org/"><img src="design/icons/pytest.svg" width="50" height="50"  alt="PyTest" title="PyTest"/></a>
<a href="https://www.selenium.dev//"><img src="design/icons/selenium.svg" width="50" height="50"  alt="Selenium" title="Selenium"/></a>
<a href="https://qameta.io/allure-report/"><img src="design/icons/allure.png" width="50" height="50"  alt="allure-report" title="allure-report"/></a>
<a href="https://aerokube.com/selenoid/"><img src="design/icons/selenoid.png" width="50" height="50"  alt="Selenoid" title="Selenoid"/></a>
<a href="https://www.jenkins.io/"><img src="design/icons/jenkins.svg" width="50" height="50"  alt="Jenkins" title="Jenkins"/></a>
<a href="https://github.com/"><img src="design/icons/github.png" width="50" height="50"  alt="Github" title="Github"/></a>
<a href="https://web.telegram.org/"><img src="design/icons/telegram.png" width="50" height="50"  alt="Telegram" title="Telegram"></a>
</p>

# Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/007-eugene0322-unit15/">Ссылка на проект в Jenkins</a>

### Параметры сборки

* COMMENT (default: @eugene0322)


## Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/007-eugene0322-unit15/">проект</a>

![This is an image](design/images/jenkins-job.png)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить параметр
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](design/images/jenkins-allure.png)

## Локальный запуск автотестов
### Перед запуском:

В папке проекта необходимо создать .env файл со следующим содержанием:
```bash
LOGIN='user1'
PASSWORD='1234'
```
Создание виртуального окружения и установка зависимостей:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Запуск:
```bash
pytest tests
```

### Получение отчёта:
```bash
allure serve
```

## Allure Отчет
##### После прохождения тестов, результаты можно посмотреть в генерируемом Allure отчете.
![This is an image](design/images/allure-report.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](design/images/allure-graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и добавлены логи, скриншот и видео.
![This is an image](design/images/allure-suits.png)

#### Пример видеозаписи прохождения теста
![This is an image](design/video/video.gif)

# Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](design/images/telegram-report.png)