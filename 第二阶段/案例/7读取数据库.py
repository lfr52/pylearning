from pymysql import Connection

conn = Connection(
    host='localhost', 
    port=3306,
    user='root',
    password='123456',
    autocommit=True  # 设置自动提交
)

cursor = conn.cursor() 
conn.select_db('py_mysql')
cursor.execute('select cast(order_data as char), order_id, money, province from orders') 
result = cursor.fetchall()
d = {}
f = open("test1.txt", "w", encoding="UTF-8-sig")
for r in result:
    d['data'] = r[0]
    d['order_id'] = r[1]
    d['money'] = r[2]
    d['province'] = r[3]
    f.write(str(d) + '\n')


f.flush()
f.close()
conn.close()