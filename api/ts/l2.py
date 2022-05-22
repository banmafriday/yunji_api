import cx_Oracle

connection = cx_Oracle.connect('query_user', 'query_user', '172.16.100.74:1521/lotsdb')
cur = connection.cursor()

sql = "select securitycode from lots.CONFIG_SYS_PHONECHECK WHERE PHONENUMBER='17267088535' ORDER BY securitycodesendtime desc".format(
    ['securitycode'])
cur.execute(sql)
result = cur.fetchone()

str = ''.join(result)
print(str)
str = ''.join(result)
