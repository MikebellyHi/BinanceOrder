Этот файл создан в рамках тестового задания
Этот файл создает ордера на бирже Binance с указанными внутри него параметрами (с заделом на получение данных и их обработку)

Чтобы запустить программу, вам необходимо:
1. Установленный Python 3.10
2. Установленная библиотека requests
3. Файл config.py, где будут храниться ключи от Binance-API

Чтобы установить Python на свой ПК, перейдите на официальный сайт, скачайте установщик и установите Python (для работы этого проекта подойдет и новейшая версия Python)
Ссылка: https://www.python.org/downloads/

Чтобы установить библиотеку requests:
1. Откройте командную строку в папке с файлом, это можно сделать двумя путями:
	а) В папке проекта кликните с зажатым Shift правой кнопкой мыши в пустом месте и нажмите "Открыть окно PowerShell здесь"
	б) Найдите командную строку через поиск в меню Пуск, перейдите в папку с помощью команды "cd". "cd .." - перемещение в директорию (папку) ниже, "cd 'Название папки'" - перейти в папку 'Название папки'
2. Введите команду "pip install requests"
3. Дождитесь корректного завершения установки, ориентируйтесь на слова "Successfully installed"

Как создать файл config.py и что в нем должно быть:
1. Нажмите в пустом месте папки проекта -> Создать -> Текстовый документ
2. Введите название "config.py", где ".py" - новое расширение, его нужно поставить вместо ".txt"
3. Согласитесь на изменение расширения файла
4. Откройте файл с помощью блокнота и введите туда следующие данные:
API_KEY = '00000000000'
API_SECRET = '00000000'
Где вместо нулей, соответственно, должны быть ваши ключи от API-Binance

Чтобы запустить проект, вам нужно:
1. Перейти в командной строке в папку проекта одним из вышеописанных способов (способы описаны в первом пункте установки библиотеки requests)
2. Ввести команду python main.py
