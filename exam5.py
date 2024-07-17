# Dehqonov Sharafbek
import psycopg2 as pg
from threading import Thread
import time


# Task 1 and 2
def task_one_and_two():
    with pg.connect(dbname='new_db',
                    user='postgres',
                    host='localhost',
                    password='1234',
                    port=5432) as conn:
        with conn.cursor() as cur:
            def create_table():
                create_table_query = ''' CREATE TABLE IF NOT EXISTS product (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        price NUMERIC(10,2) NOT NULL,
                        color VARCHAR(60),
                        image VARCHAR(255));'''

                cur.execute(create_table_query)
                conn.commit()

            def insert_product():
                insert_into_query = """INSERT INTO product (name, price) 
                VALUES (%s, %s);"""
                cur.execute(insert_into_query)
                conn.commit()

            def update_product():
                update_query = """UPDATE product SET name = %s, price = %s, color = %s, image = %s;"""
                data = ('name1', 'price1', 'color1', 'image1')
                cur.execute(update_query, data)
                conn.commit()

            def select_all_product():
                select_all_product = """SELECT * FROM product ;"""
                cur.execute(select_all_product)
                cur.fetchall()

            def delete_product():
                delete_into_query = """DELETE FROM product where id = %s;"""

                cur.execute(delete_into_query)
                conn.commit()

    def my_menu():
        while True:
            # Menu yaratib mukammalroq qilmoqchi edim
            create_table()
            pass

    my_menu()


def task_three():
    class Alphabet:
        def init(self, letters):
            self.letters = letters
            self.index = 0

        def iter(self):
            return self

        def next(self):
            if self.letters.index < len(self.letters):
                leter = self.letters[self.letters.index]
                self.index += 1
                return self.letters[leter]
            else:
                raise StopIteration

    letter = Alphabet('ABCDEFGHIJKLMNOREPUJKLMNOW')

    for result in letter:
        print(result)


def task_four():
    def print_numbers():
        for i in range(1, 6):
            print(i)
            time.sleep(1)

    # def print_letters():
    #     word = 'ABCDE'
    #     for i in word:
    #         print(i)
    #         time.sleep(1)
    def print_letters():
        for i in ['A', 'B', 'C', 'D', 'E']:
            print(i)
            time.sleep(1)

    numbers = Thread(target=print_numbers)
    letters = Thread(target=print_letters)

    numbers.start()
    letters.start()
    numbers.join()
    letters.join()


def task_five():
    my_db = {
        'database': 'new_db',
        'host': 'localhost',
        'user': 'postgres',
        'password': '1234',
        'port': 5432
    }

    class Product:
        def __init__(self, id: int | None = None, name: str | None = None, price: int | None = None):
            self.id = id
            self.name = name
            self.price = price

        def save(self):
            with DbConnect(my_db) as cursor:
                insert_query = 'INSERT INTO test.product(name, price) values (%s, %s);'
                insert_params = (self.name, self.price)
                cursor.execute(insert_query, insert_params)


def task_six():
    my_db = {
        'database': 'new_db',
        'host': 'localhost',
        'user': 'postgres',
        'password': '1234',
        'port': 5432
    }

    class DbConnect:
        def __init__(self, db_key):
            self.db_key = my_db
            self.conn = None
            self.cur = None

        def __enter__(self):
            self.conn = pg.connect(**self.db_key)
            self.cur = self.conn.cursor()
            self.conn.commit()
            return self.cur

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.cur is not self.cur.closed:
                self.cur.close()
            if self.conn is not self.conn.closed:
                self.conn.close()

    with DbConnect('postgres') as db:
        pass


def task_seven():
    pass


def task_eight():
    """
    git init
    git status
    git add .
    git commit -m "Exam of module 5"
    git remote add origin https://github.com/Sharafbek/exam_5.git
    git push origin master
    """
    pass


"""

7. https://dummyjson.com/products/ urlga so’rov yuborib , kelgan ma’lumotlarni Product nomli tabelga saqlang
	=> 12.5 ball

8.Yechgan misollaringni git commandalari orqali githubga add qilinglar.
	12.5 -  ball


"""
