"""Скрипт для заполнения данными таблиц в БД Postgres."""
# Импортируются необходимые модули psycopg2 и csv
import psycopg2
import csv

# Создается соединение с базой данных PostgreSQL с помощью функции psycopg2.connect(), передавая в нее параметры
# подключения: имя хоста, имя базы данных, имя пользователя и пароль
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="231287")

try:
    with conn:
        # Создается курсор для выполнения операций с базой данных с помощью метода conn.cursor()
        with conn.cursor() as cur:
            """Получение данных из таблицы employees_data.csv"""
            # Открывается файл employees_data.csv с помощью функции open().
            with open('north_data/employees_data.csv', newline='', encoding='utf-8') as csvfile:
                # Создается объект csv.reader() для чтения данных из файла CSV с заданными параметрами
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                # С помощью функции next() пропускается первая строка файла CSV, содержащая заголовки столбцов.
                next(reader)
                # В цикле for происходит итерация по строкам файла CSV, и для каждой строки выполняется SQL-запрос на
                # вставку данных в таблицу базы данных с помощью метода cur.execute
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", row)

            """Получение данных из таблицы customers_data.csv"""
            with open('north_data/customers_data.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s)", row)

            """Получение данных из таблицы orders_data.csv"""
            with open('north_data/orders_data.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", row)
finally:
    # Закрывается курсор с помощью метода cur.close().
    # Закрывается соединение с базой данных с помощью метода conn.close()
    conn.close()