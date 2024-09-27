import  sqlite3

# Подключаемся к базе данных
conn=sqlite3.connect("delivery.db",check_same_thread=False)
sql=conn.cursor()

#Создание таблицы пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name TEXT, number TEXT);')

#Создание таблицы продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, pr_name TEXT, pr_price REAL, pr_count INTEGER, pr_photo TEXT);')

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