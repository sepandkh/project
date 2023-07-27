import sqlite3

cnt=sqlite3.connect("shop.db")

def get_products():
    sql='''SELECT * FROM products '''
    result=cnt.execute(sql)
    row=result.fetchall()
    return row
def get_single_product(id1):
    sql='''SELECT * FROM products WHERE id=?'''
    result=cnt.execute(sql,(id1,))
    row=result.fetchone()
    return row
def save_to_cart(pid,uid,qnt):  
    sql='''INSERT INTO cart (pid,uid,qnt)
                VALUES(?,?,?)'''
    cnt.execute(sql,(pid,uid,qnt))
    cnt.commit()
def qnt_of_product(pid):
    sql='''SELECT qnt  FROM products WHERE id=?'''
    result=cnt.execute(sql,(pid,))
    row=result.fetchone()
    return row
                
def update_prodect_table(pid,qnt):
    result=qnt_of_product(pid)
    Pqnt=result[0]
    sql='''UPDATE products SET qnt=? WHERE id=?'''
    Nqnt=Pqnt-qnt
    cnt.execute(sql,(Nqnt,pid))
    cnt.commit()
def add_product(pid,qnt):
    result=qnt_of_product(pid)
    Pqnt=result[0]
    sql='''UPDATE products SET qnt=? WHERE id=?'''
    Nqnt=Pqnt+qnt
    cnt.execute(sql,(Nqnt,pid))
    cnt.commit()
def add_new_product(pname,pprice,qnt):
    sql='''INSERT INTO products 
              (pname,price,qnt)
              VALUES(?,?,?)'''
    cnt.execute(sql,(pname,pprice,qnt)) 
    cnt.commit()         
    










