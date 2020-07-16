# import sqlite3
# #
# connect=sqlite3.connect('swt.db')
# c=connect.cursor()
# # c.execute('''CREATE TABLE COMPANY
# #        (ID INT PRIMARY KEY     NOT NULL,
# #        NAME           TEXT    NOT NULL,
# #        AGE            INT     NOT NULL,
# #        ADDRESS        CHAR(50),
# #        SALARY         REAL);''')
#
# # c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
# #       VALUES (1, 'Paul', 32, 'California', 20000.00 )")
# c.execute('''CREATE TABLE MOVIE(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME CHAR(20),URL CHAR(50));''')
# c.execute("INSERT INTO MOVIE('name','url') VALUES (‘swtinfo’,'https://www.baidu.com')")
# c.execute("INSERT INTO MOVIE ('name','url') VALUES ('swt111','https://www.baidu.com')")
# connect.commit()
# connect.close()