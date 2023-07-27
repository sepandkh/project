import sqlite3

cnt=sqlite3.connect("shop.db")

#==================== create users table ===============
#
# sql='''CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     user CHAR(15) NOT NULL,
#     pass CHAR(25) NOT NULL,
#     addr CHAR(50),
#     score INTEGER)'''
# cnt.execute(sql)
# print("Table has created")
#===================== insert data into table ===========
# sql='''INSERT INTO users 
#         (user,pass,addr,score)
#         VALUES("lina","12121212lina","rodbar",4)'''
# cnt.execute(sql)
# cnt.commit()
#========================== create product table =====================

# sql='''CREATE TABLE products (
#         id INTEGER PRIMARY KEY,
#         pname CHAR(15) NOT NULL,
#         price  INTEGER NOT NULL,
#         qnt INTEGER 
#             )'''
# cnt.execute(sql)
# print("table product has been creted")
#==================================== insert data to products table =============================
# sql='''INSERT INTO products 
#         (pname,price,qnt)
#         VALUES("pen","20","6")'''
# cnt.execute(sql)
# cnt.commit()
#==================================== create cart table ====================
# sql='''CREATE TABLE cart (
#          id INTEGER PRIMARY KEY,
#          pid INTEGER NOT NULL,
#          uid INTEGER NOT NULL,
#          qnt INTEGER  NOT NULL
#         )'''
# cnt.execute(sql)
# print("the table cart has created")

#========================== create data login_block =========================

# sql='''CREATE TABLE login_block (
#             id INTEGER PRIMARY KEY,
#             user CHAR(15) NOT NULL)'''

# cnt.execute(sql)         
# print("Table has created")







