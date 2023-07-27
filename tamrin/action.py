import sqlite3

cnt=sqlite3.connect("shop.db")


def user_login(user,pas):
    cnt=sqlite3.connect("shop.db")
    sql=''' SELECT * FROM users WHERE user=? and pass=?'''
    result=cnt.execute(sql,(user,pas))
    rows=result.fetchall()
    if len(rows)<1:
        return False
    else:
        return rows[0][0]
    
    
    
def user_submit(user,pas):
    if len(pas)<8:
        return False,"password length error!"
    elif pas.isalpha() or pas.isdigit():
        return False,"password combination error!"
    
    sql='''SELECT * FROM users WHERE user=?'''
    result=cnt.execute(sql,(user,))
    rows=result.fetchall()
    if len(rows)>0:
        return False,"username already exist!"
    sql='''INSERT INTO users (user,pass,score) VALUES (?,?,?)'''
    cnt.execute(sql,(user,pas,5))
    cnt.commit()
    return True,""
def add_block_user(name):
    sql='''INSERT INTO login_block (user) VALUES (?)'''
    cnt.execute(sql,(name,))
    cnt.commit()
def block_user(name):
    sql='''SELECT * FROM login_block WHERE user=?'''
    result=cnt.execute(sql,(name,))
    row=result.fetchall()
    if len(row)==0:
        return True
    else:
        return False
    
def get_score(user):
    sql='''SELECT score FROM users WHERE user=?'''
    result=cnt.execute(sql,(user,))
    row=result.fetchone()
    if(int(row[0]))>=5:
        return True
    else:
        return False

            
        
    
    
    
    
    
    
    
    
    
        
    
    