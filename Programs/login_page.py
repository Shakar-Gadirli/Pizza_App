from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from Programs import db_for_customer
# with sqlite3.connect('username_database.db') as db:
# 	c = db.cursor()
db = sqlite3.connect("username_database.db")
c=db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL);')
# db.commit()
# db.close()

#class main:
# def __init__(self):
# # Window 
# # self.master = master
# # Some Usefull variables
# self.username = StringVar()
# self.password = StringVar()
# self.n_username = StringVar()
# self.n_password = StringVar()
# #Create Widgets
# #self.widgets()
def login(username,password):
    try:
        with sqlite3.connect('username_database.db') as db:
            c=db.cursor()

		#Find user If there is any take proper action
        u_p=(username,password)
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,u_p)
        result = c.fetchone()
        c.close()
    except sqlite3.Error as error:
        print("Failed to Log in ",error)
    finally:
        if(db):
            db.close()


    if result:
        #     #self.logf.pack_forget()
        #     self.head['text'] = self.username.get() + '\n Logged In'
        #     self.head['pady'] = 150
        # else:
        #     ms.showerror('Oops!','Username Not Found.')
        #     #return "Username not found"
        return True
    else:
        return False

def new_user(username,password):
    	#Establish Connection
    with sqlite3.connect('username_database.db') as db:
        c = db.cursor()
    u_p=(username,password)
    
    find_user = ('SELECT * FROM user WHERE username = ?')
    c.execute(find_user,(username,))
    respond=c.fetchone()
    if respond:
        ms.showerror('Error!','Username Taken Try a Different One.')
        return 'Error! Username Taken Try a Different One.'
    else:
        #self.log()
        send="""INSERT INTO user (username,password) VALUES (?,?)"""
        c.execute(send,u_p)
        db.commit()
        db_for_customer.create(username)
        ms.showinfo('Success!  Account Created!')
        return 'Success!  Account Created!'
    c.close()
    db.close()

def search(username):
    
    c=sqlite3.connect('username_database.db')
    cur=c.cursor()
    q="SELECT * FROM user  WHERE username = ?"
    cur.execute(q,(username,))
    return cur.fetchone()
    cur.close()
    c.close()
    # def log(self):
    #     self.username.set('')
    #     self.password.set('')
    #     self.crf.pack_forget()
    #     self.head['text'] = 'LOGIN'
    #     self.logf.pack()
    # def cr(self):
    #     self.n_username.set('')
    #     self.n_password.set('')
    #     self.logf.pack_forget()
    #     self.head['text'] = 'Create Account'
    #     self.crf.pack()
        
    # #Draw Widgets
    # def widgets(self):
    #     self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
    #     self.head.pack()
    #     self.logf = Frame(self.master,padx =10,pady = 10)
    #     Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
    #     Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
    #     Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
    #     Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
    #     Button(self.logf,text = ' Log`in ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
    #     Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
    #     self.logf.pack()
        
    #     self.crf = Frame(self.master,padx =10,pady = 10)
    #     Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
    #     Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
    #     Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
    #     Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
    #     Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
    #     Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

    

#create window and application object
# root = Tk()
# #root.title("Login Form")
# main(root)
# root.mainloop()