import tkinter
import sqlite3
from action import *
from productAction import *

def login():
    global counter
    global session
    user=txt_user.get()
    pas=txt_pass.get()
    result=user_login(user,pas)
    if counter==2:
        btn_login.configure(state="disabled")
    name1=block_user(user)
    name2=get_score(user)
    print(name1)
    if not name1:
        lbl_msg.configure(text="welcome to your account",fg="green")
        btn_login.configure(state="disabled")
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
        btn_logout.configure(state="active")
        session=result
        
        
    else: 
        if not name2:
            lbl_msg.configure(text="welcome to your account",fg="green")
            btn_login.configure(state="disabled")
            txt_user.delete(0,"end")
            txt_pass.delete(0,"end")
            btn_logout.configure(state="active")
            session=result
        else:
            if result:
                lbl_msg.configure(text="welcome to your account",fg="green")
                btn_login.configure(state="disabled")
                txt_user.delete(0,"end")
                txt_pass.delete(0,"end")
                btn_logout.configure(state="active")
                btn_shop.configure(state="active")
                session=result
                if(user=="admin"):
                    btn_AdminPanel.configure(state="active")
                    
                
            else:    
                lbl_msg.configure(text="wrong username or password",fg="red")
                counter+=1
    
def submit(): 
    user=txt_user.get()
    pas=txt_pass.get()
    result,errormsg=user_submit(user,pas)
    if result:
       lbl_msg.configure(text="submit done!",fg="green")  
    else:
       lbl_msg.configure(text=errormsg ,fg="red")      
    
def logout():
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")
    lbl_msg.configure(text="you are logout now",fg="orange")
    btn_shop.configure(state="disabled")
    btn_AdminPanel.configure(state="disabled")
def shop():
    def buy():
        pid=pidtxt.get()
        qnt=pqnttxt.get()
        if(pid=="" or qnt==""):
            lbl_msg2.configure(text="fill the inputs",fg="red")
            return
        if not pid.isdigit() or not qnt.isdigit():
            lbl_msg2.configure(text="you must enter a number in inputs !!!",fg="red")
            return
        result=get_single_product(pid)
        
        if not result:
            lbl_msg2.configure(text="wrong product id",fg="red")
            return
        if int(qnt)>result[3]:
            lbl_msg2.configure(text="not enough producs",fg="red")
            return
        if int(qnt)<=0:
            lbl_msg2.configure(text="quantity should be at least 1",fg="red")
            return
        save_to_cart(pid,session,qnt) 
        update_prodect_table(pid,int(qnt))
        #
        products=get_products()
        lst.delete(0,"end")
        for product in products:
            text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
            lst.insert("end",text)
        lbl_msg2.configure(text="add to cart successfully",fg="green")
        pidtxt.delete(0,"end")
        pqnttxt.delete(0,"end")
            
    win_shop=tkinter.Toplevel(win)
    win_shop.geometry("400x400")
    win_shop.title("shopping panel")
    
    lst=tkinter.Listbox(win_shop,width=50)
    lst.pack()
    
    products=get_products()
    #sprint(products)
    for product in products:
        text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
        lst.insert("end",text)
        
    pidlbl=tkinter.Label(win_shop,text="ID: ")
    pidlbl.pack()
    
    pidtxt=tkinter.Entry(win_shop)
    pidtxt.pack()
    
    pqntlbl=tkinter.Label(win_shop,text="QUANTITY: ")
    pqntlbl.pack()
    
    pqnttxt=tkinter.Entry(win_shop)
    pqnttxt.pack()
    
    btn_buy=tkinter.Button(win_shop,text="BUY",command=buy)
    btn_buy.pack()
    
    lbl_msg2=tkinter.Label(win_shop,text="")
    lbl_msg2.pack()

    win_shop.mainloop()
def AdminPanel():
    def old():
        def add():
           pid=pidtxt.get()
           qnt=pqnttxt.get()
           if(pid=="" or qnt==""):
               lbl_msg2.configure(text="fill the inputs",fg="red")
               return
           if not pid.isdigit() or not qnt.isdigit():
               lbl_msg2.configure(text="you must enter a number in inputs !!!",fg="red")
               return
           result=get_single_product(pid)
           
           if not result:
               lbl_msg2.configure(text="wrong product id",fg="red")
               return
           add_product(pid,int(qnt))
           lbl_msg2.configure(text="product added",fg="green")
           pidtxt.delete(0,"end")
           pqnttxt.delete(0,"end")
           
           
           products=get_products()
           #sprint(products)
           lst.delete(0,"end")
           for product in products:
               text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
               lst.insert("end",text)
           
           
        win_old=tkinter.Toplevel(win)
        win_old.geometry("400x400")
        win_old.title("old products panel")
        
        lst=tkinter.Listbox(win_old,width=50)
        lst.pack()
        

        
        products=get_products()
        #sprint(products)
        for product in products:
            text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
            lst.insert("end",text)
        pidlbl=tkinter.Label(win_old,text="ID: ")
        pidlbl.pack()
        
        pidtxt=tkinter.Entry(win_old)
        pidtxt.pack()
        
        pqntlbl=tkinter.Label(win_old,text="QUANTITY: ")
        pqntlbl.pack()
        
        pqnttxt=tkinter.Entry(win_old)
        pqnttxt.pack()
        
        btn_add=tkinter.Button(win_old,text="add",command=add)
        btn_add.pack()
        
        lbl_msg2=tkinter.Label(win_old,text="")
        lbl_msg2.pack()
        win_old.mainloop()
            
    def new():
        def add():
            pname=pnametxt.get()
            pprice=ppricetxt.get()
            qnt=pqnttxt.get()
            if(pprice=="" or qnt=="" or pname==""):
                lbl_msg2.configure(text="fill the inputs",fg="red")
                return
            add_new_product(pname,pprice,qnt)
            print("the new product added")
        win_new=tkinter.Toplevel(win)
        win_new.geometry("400x400")
        win_new.title("new products panel")

        
        pnamelbl=tkinter.Label(win_new,text="NAME: ")
        pnamelbl.pack()
        
        pnametxt=tkinter.Entry(win_new)
        pnametxt.pack()
        
        ppricelbl=tkinter.Label(win_new,text="PRICE: ")
        ppricelbl.pack()
        
        ppricetxt=tkinter.Entry(win_new)
        ppricetxt.pack()
        
        pqntlbl=tkinter.Label(win_new,text="QUANTITY: ")
        pqntlbl.pack()
        
        pqnttxt=tkinter.Entry(win_new)
        pqnttxt.pack()
        
        
        btn_add=tkinter.Button(win_new,text="add",command=add)
        btn_add.pack()
        
        lbl_msg2=tkinter.Label(win_new,text="")
        lbl_msg2.pack()
        
        win_new.mainloop()

        
    def buy_block():
        def block():
            global name
            name=bbuytxt.get()
            print(name)
            add_block_user(name)
            bbuytxt.delete(0,"end") 
        
        win_bblock=tkinter.Toplevel(win)
        win_bblock.geometry("400x400")
        win_bblock.title("buy block panel")

        
        bbuylbl=tkinter.Label(win_bblock,text="user of the person : ")
        bbuylbl.pack()
        
        bbuytxt=tkinter.Entry(win_bblock)
        bbuytxt.pack()
        
        btn_ok=tkinter.Button(win_bblock,text="ok",command=block)
        btn_ok.pack()
        
        
        
        win_bblock.mainloop()
        
    
    win_admin=tkinter.Toplevel(win)
    win_admin.geometry("400x400")
    win_admin.title("admin panel")
    
    btn_one=tkinter.Button(win_admin,text="add to old products",command=old)
    btn_one.pack()
    
    btn_two=tkinter.Button(win_admin,text="add a new product",command=new)
    btn_two.pack()
    
    btn_bbuy=tkinter.Button(win_admin,text="block buy",command=buy_block)
    btn_bbuy.pack()
    
    

    
    win_admin.mainloop()
#==================================================
session=""
counter=0
name=""

win=tkinter.Tk()
win.geometry("300x300")

lbl_user=tkinter.Label(win,text="username: ")
lbl_user.pack()
txt_user=tkinter.Entry(win)
txt_user.pack()

lbl_pass=tkinter.Label(win,text="password: ")
lbl_pass.pack()
txt_pass=tkinter.Entry(win)
txt_pass.pack()

lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()

btn_login=tkinter.Button(win,text="login",command=login)
btn_login.pack()

btn_submit=tkinter.Button(win,text="submit",command=submit)
btn_submit.pack()

btn_logout=tkinter.Button(win,text="logout",state="disabled",command=logout)
btn_logout.pack()

btn_shop=tkinter.Button(win,text="shop",state="disabled",command=shop)
btn_shop.pack()

btn_AdminPanel=tkinter.Button(win,text="Admin Panel",state="disabled",command=AdminPanel)
btn_AdminPanel.pack()



win.mainloop()