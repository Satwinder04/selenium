insert_query="insert into Student values(104,'kim',89)"
update_query="update Student set NAME='Mary' where ID=104"
deletle_query="delete from Student where ID=2"

import pymysql

try:
    con=pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="youtube"
    )
    curs=con.cursor()
    curs.execute(insert_query)
    curs.execute(update_query)
    curs.execute(deletle_query)
    curs.execute("select * from Student")

    for row in curs:
        print(row[0],row[1],row[2])

    # for i in curs:
    #     print(i[0],i[1],i[2])

    con.close()
except:
    print("database not connected")