
# 链接到数据库
from pymysql import Connection

conn = Connection(
    host='localhost', 
    port=3306,
    user='root',
    password='123456',
    autocommit=True  # 设置自动提交
)

print(conn.get_server_info())

# 执行非查询性质sql
# cursor = conn.cursor() # 得到游标对象
# conn.select_db('test') # 选择数据库
# cursor.execute('create table py_mysql(id int)') # 执行sql语句

# 执行查询性质sql
# cursor = conn.cursor() # 得到游标对象
# conn.select_db('world') # 选择数据库
# cursor.execute('select * from student') # 执行sql语句
# result = cursor.fetchall()  # 得到一个嵌套元组，每一个元素也是一个元组
# print(result)
# for r in result:
#     print(r)

# 插入数据
cursor = conn.cursor() 
conn.select_db('world') 
cursor.execute("insert into student values (10002, 'lin', 31, '男')") # 执行sql语句
# conn.commit() # 确认机制
conn.close()