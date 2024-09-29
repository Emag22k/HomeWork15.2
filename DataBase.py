import  sqlite3
from logging import fatal

# Подключаемся к базе данных
conn=sqlite3.connect("delivery.db",check_same_thread=False)
sql=conn.cursor()

#Создание таблицы пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name TEXT, number TEXT);')

#Создание таблицы продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products(pr_id INTEGER PRIMARY KEY AUTOINCREMENT,pr_des, pr_name TEXT, pr_price REAL, pr_count INTEGER, pr_photo TEXT);')

#Создание таблицы корзины
sql.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, user_product TEXT, product_amount INTEGER);')


## Метод для пользователя##

#Регистрация пользователя в БД
def register(tg_id,name,number):
    sql.execute('INSERT INTO users VALUES (?,?,?);', (tg_id,name,number))
    conn.commit()

#Проверка пользователя в БД
def rechek(tg_id):
    if sql.execute('SELECT * FROM users WHERE tg_id=?;', (tg_id,)).fetchone():
        return True
    else:
        return False


##Методы для продуктов:


#Вывод продуктов для кнопок:
def get_pr_buttons():
    all_products=sql.execute("SELECT * FROM products;").fetchall()
    result= [i for i in all_products if i[4]>0]
    return result


#Вывод информации о конкретном продукте:
def get_exact_pe(pr_id):
    return sql.execute("SELECT * FROM products WHERE pr_id=?;", (pr_id,)).fetchone()


#Вывод цены конкретного продукта:
def get_exact_price(pr_id):
    return sql.execute("SELECT * FROM products WHERE pr_id=?;", (pr_id,)).fetchone()


##Методы для Админестрирования продуктов

#Добавление продукта в ДБ
def pr_to_db(pr_name,pr_price,pr_count,pr_photo,pr_des):
    if pr_name in sql.execute("SELECT pr_name FROM products;").fetchall():
        return False
    else:
        sql.execute("INSERT INTO products(pr_name,pr_des,pr_price,pr_count,pr_photo) VALUSE (?,?,?,?,?)",(pr_name,pr_des,pr_price,pr_count,pr_photo))
        conn.commit()

#Изменение аттрибута продукта:
def change_pr_attr(keyword, new_value, attr=""):
    if attr == "name":
        sql.execute("UPDATE prouducts SET pr_name=? WHERE pr_name=?;", (new_value,keyword))
    elif attr == "description":
        sql.execute("UPDATE products SET pr_des=? WHERE pr_name=?", (new_value,keyword))
    elif attr == "price":
        sql.execute("UPDATE products SET pr_price=? WHERE pr_name=?", (new_value, keyword))
    elif attr == "count":
        sql.execute("UPDATE products SET pr_count=? WHERE pr_name=?", (new_value,keyword))
    elif attr == "photo":
        sql.execute("UPDATE products SET pr_photo=? WHERE pr_name=?", (new_value,keyword))

    conn.commit()

#Удаление товара из БД
def del_product(pr_id):
    sql.execute('DELETE FROM products WHERE pr_id=?;', (pr_id,))
    conn.commit()

#Проверка товаров на наличие:
def check_pr():
    if sql.execute("SELECT * FROM products ;").fetchall():
        return True
    else:
        return False