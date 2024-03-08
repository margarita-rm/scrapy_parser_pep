## Описание проекта парсинга

Парсер "pep" парсит данные обо всех документах PEP, считает количество PEP в каждом статусе и общее количество PEP, сохраняет результат в табличном виде в csv-файлы.

### Автор:
Маргарита Мифтахова

[Telegram](https://t.me/margarita_rm)

### Cтек используемых технологий:  
Python, Scrapy

### Как развернуть проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/margarita-rm/scrapy_parser_pep
```
```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Команда запуска:

```
scrapy crawl pep
```
