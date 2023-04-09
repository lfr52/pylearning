import data_define
from file_define import TextFileReader
from file_define import JsonFileReader
from pymysql import Connection

text_file_reader = TextFileReader('H:/pylearning/第二阶段/2011年1月销售数据.txt')
jan_data = text_file_reader.read_data()

json_file_reader = JsonFileReader('H:/pylearning/第二阶段/2011年2月销售数据JSON.txt')
feb_data = json_file_reader.read_data()

all_data = jan_data + feb_data

conn = Connection(
    host='localhost', 
    port=3306,
    user='root',
    password='123456',
    autocommit=True  # 设置自动提交
)

cursor = conn.cursor() 
conn.select_db('py_mysql')
for record in all_data:
    sql = f"insert into orders(order_data, order_id, money, province) " \
          f"values('{record.order_data}', '{record.order_id}', {record.money}, '{record.province}')" 
    cursor.execute(sql)

conn.close()