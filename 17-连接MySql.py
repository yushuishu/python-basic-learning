# -*- coding: utf-8 -*-
"""
@Time ：2022-11-12 22:51
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)

需要下载 pip install pymysql
"""

from pymysql import Connection

# 构建mysql数据库连接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("test")
# 创建表
cursor.execute("drop table if exists test_python")
cursor.execute('''
    CREATE TABLE test_python(
        `id` int(11) not null AUTO_INCREMENT PRIMARY key,
        `name` varchar(255) default null
    )engine=innodb default charset=utf8;
''')

# 插入
cursor.execute("insert into test_python values(1001, '张三');")
cursor.execute("insert into test_python values(1002, '李四');")

# 执行查询SQL
cursor.execute("select * from test_python")
results = cursor.fetchall()
print(results)

# 关闭链接
conn.close()
