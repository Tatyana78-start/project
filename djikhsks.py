import psycopg2

# Подключение к базе данных
conn = psycopg2. connect(
    dbname='test1',
    user='postgres',
    password='Pies',
    host='localhost',
    port=5432
)

# Создание курсора для выполнения запроса
cur = conn.cursor()

# Отправляем запрос на получение всех данных из таблицы categories
cur.execute("""select distinct contact_name
                from customers
                left join orders using (customer_id)
                 where order_id is NOT Null
                 order by contact_name""")

# Получение результата
rows = cur.fetchall()
for row in rows:
    print(*row)

#Закрытие курсора и соединение с базой
cur.close()
conn.close()




