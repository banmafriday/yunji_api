import cx_Oracle as cx
con = cx.connect('query_user','query_user','172.16.100.74:1521/lotsdb')
cursor = con.cursor("select securitycode from lots.CONFIG_SYS_PHONECHECK WHERE PHONENUMBER='17267088535'  ORDER BY securitycodesendtime desc;")
data = cursor.fetchone()        #获取一条数据
print(data)     #打印数据
cursor.close()  #关闭游标
con.close()     #关闭数据库连接
print(con)
result = print()
