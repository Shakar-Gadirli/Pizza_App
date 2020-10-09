from Programs import login_page
from Programs import admin_page
from Programs import db_for_customer
from Programs import pizza
from Programs import *


from PIL import ImageTk
import PIL.Image 
import os

from tkinter import messagebox as ms
import sqlite3
import tkinter as tk
from tkinter import *

class PizzaApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("ORDER PIZZA")
		self.frame=None
		self.geometry("750x750")
		self.configure(bg='azure')
		self.change_page(Login)

	def change_page(self,page_c):
		next_page=page_c(self)
		if self.frame is not None:
			self.frame.destroy()
		self.frame=next_page
		self.frame.pack()


global customer

def login(frame,username,password):
	if username=='admin' and password=='admin':
		frame.master.change_page(Admin)
		return

	global customer
	customer=username
	r=login_page.login(username,password)
	if r:
		frame.master.change_page(MainMenu)
	else:
		frame.fail=tk.Label(frame,text='Wrong username or password! ')
		frame.fail.grid(row=8)
class Login(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self,master)
		self.master=master
		self.username=StringVar()
		self.password=StringVar()
		self.n_username=StringVar()
		self.n_password=StringVar()
		#self.head['text'] = 'LOGIN'
		self.configure(bg="azure")
		tk.Label(self,text = 'Username: ',bg="azure",font = ('',20),pady=5,padx=5).grid(sticky = W)
		tk.Entry(self,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
		tk.Label(self,text = 'Password: ',bg="azure",font = ('',20),pady=5,padx=5).grid(sticky = W)
		tk.Entry(self,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
		tk.Button(self,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: login(self,self.username.get(),self.password.get())).grid()
		tk.Button(self,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: master.change_page(Sign_Up)).grid(row=2,column=1)
		#self.logf.pack()
        
		#self.widgets()
	def log(self):
		self.username.set('')
		self.password.set('')
		self.crf.pack_forget()
		self.head['text'] = 'LOGIN'
		self.logf.pack()
	def cr(self):
		self.n_username.set('')
		self.n_password.set('')
		self.logf.pack_forget()
		self.head['text'] = 'Create Account'
		#self.crf.pack()
	
	# tk.Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
	# tk.Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
    
 #    #Draw Widgets
	# def widgets(self):
	# 	self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
	# 	self.head.pack()
		#self.logf = Frame(self.master,padx =10,pady = 10)
		# tk.Label(self,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
		# tk.Entry(self,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
		# tk.Label(self,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
		# tk.Entry(self,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
		# tk.Button(self,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: login(self,self.username.get(),self.password.get())).grid()
		# tk.Button(self,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
		# self.logf.pack()
        


def sign_up(frame,username,password):
	login_page.new_user(username,password)
 	#frame.text=tk.Label(frame,text=respond,)

	
class Sign_Up(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self,master)
		self.master=master
		self.n_username=StringVar()
		self.n_password=StringVar()
		self.configure(bg="azure")
		Label(self,text = 'Username: ',bg="azure",font = ('',20),pady=5,padx=5).grid(sticky = W)
		Entry(self,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
		Label(self,text = 'Password: ',bg="azure",font = ('',20),pady=5,padx=5).grid(sticky = W)
		Entry(self,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
		Button(self,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: sign_up(self,self.n_username.get(),self.n_password.get())).grid()
		Button(self,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: master.change_page(Login)).grid(row=2,column=1)
		#self.widgets()
	def log(self):
		self.username.set('')
		self.password.set('')
		self.crf.pack_forget()
		self.head['text'] = 'LOGIN'
		self.logf.pack()
	def cr(self):
		self.n_username.set('')
		self.n_password.set('')
		self.logf.pack_forget()
		self.head['text'] = 'Create Account'
		self.crf.pack()
	#def widgets(self):

		#self.crf = Frame(self.master,padx =10,pady = 10)
		# Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
		# Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
		# Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
		# Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
		# Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: sign_up(self,self.n_username.get(),self.n_password.get())).grid()
		# Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: self.log).grid(row=2,column=1)

ls=[0]
i=0

def incre():
	global ls
	global i
	i+=1
	ls.append(0)
def decre():
	global ls
	global i
	if i>0:
		del ls[i]
		i-=1
def make_pizza(type_of_pizza,row=None):
	global ls
	ls[i]=pizza.Pizza_Builder(type_of_pizza,row)

class MainMenu(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self,master)
		self.configure(bg='azure')
		Label(self,text="Main Menu",bg='azure',font = ('',20))
		file=open("Programs/notifications.txt","r+")
		res=file.read()
		file.close()
		Label(self,text=res,bg='azure',font = ('',20))
		# self.image_s = ImageTk.PhotoImage(Image.open("image/supreme.png"))
		# #self.image_s=tk.PhotoImage(file="image/supreme.png")
		# self.image_h=tk.PhotoImage(file="image/hawaiian.png")
		# tk.Label(self, image=self.image_s, bg="azure").grid(row=0, column=0)
		# tk.Label(self, image=self.image_h, bg="azure").grid(row=0, column=2)
		# Label(self, image=self.image_s).pack(side='bottom')
		# Label(self, image=self.image_s, bg="gray").grid(row=1, column=0)
		Button(self,text="Supreme",bg="aquamarine",fg="blue2",bd=3,font = ('',15),padx=5,pady=5,command=lambda: [make_pizza("Supreme"),master.change_page(Toppings)]).grid(row=5,column=0)

		# Label(self, image=self.image_h).pack(side='bottom')
		# Label(self, image=self.image_h, bg="gray").grid(row=1, column=1)
		Button(self,text="Hawaiian",bg="aquamarine",fg="blue2",bd=3,font = ('',15),padx=5,pady=5,command=lambda: [make_pizza("Hawaiian"),master.change_page(Toppings)]).grid(row=5,column=2)
		lis=admin_page.choose_all_data()
		if lis is not None:
			for r in lis:
				Button(self,text=r[0],bd=3,command=lambda: [make_pizza("Pizza",r),master.change_page(Toppings)]).grid()
		Button(self,text="Pizza Order History",bg="aquamarine",fg='blue2',command=lambda: master.change_page(Db_Customer)).grid(row=8,column=1)
		Button(self,text="Log Out",bg="aquamarine",fg='blue2',command=lambda: master.change_page(Login)).grid(row=9, column=1)

def new_pizza(frame,name,status,price):
	if(name=="" or price=="" or status==""):
		ms.showinfo("There is empty field!")
		return
	ans=admin_page.add_pizza(name,status,price)
	tk.Label(frame, text=ans,bg="azure").grid(row=3, column=2)
class Admin(tk.Frame):
	def __init__(self,master):
		self.master=master
		tk.Frame.__init__(self,master)
		self.configure(bg="azure")
		Label(self,text = 'name of pizza:',bg="azure",font = ('',20),pady=5,padx=5).grid(row=0,column = 0)
		self.name=tk.Entry(self)
		self.name.grid(row=0,column=1)
		Label(self,text = 'ingredients: ',bg="azure",font = ('',20),pady=5,padx=5).grid(row=1,column=0)
		self.status=tk.Entry(self)
		self.status.grid(row=1,column=1)
		Label(self,text = 'price: ',bg="azure",font = ('',20),pady=5,padx=5).grid(row=2,column=0)
		self.price=tk.Entry(self)
		self.price.grid(row=2,column=1)
		Button(self,text="Add new pizza",fg="blue2",bg="aquamarine",
			command=lambda: new_pizza(self,self.name.get(),self.status.get(),self.price.get())).grid(row=3,column=1)
		Label(self,text = 'Customer Info',bg="azure",font = ('',20),pady=5,padx=5).grid(sticky = W)
		self.username=tk.Entry(self)
		self.username.grid(row=4,column=1)

		Button(self,text="Customer Info",fg="blue2",bg="aquamarine",
			command=lambda: [self.get_info(self.username.get()),self.look_for(self.username.get())]).grid(row=5,column=1)
		Button(self,text="Log Out",fg="blue2",bg="aquamarine",command=lambda: master.change_page(Login)).grid(row=6,column=1)


	def look_for(self,username):
		if username:
			ls = login_page.search(username)
			s = "Username: " + ls[0] + "\n" + "Password: " + ls[1]
			self.t_w = tk.Text(self)
			self.t_w.grid(row=10, column=1)
			self.t_w.insert(tk.END, s)
			
			

	def get_info(self,username):
		if username:
			s=''
			l=db_for_customer.getting_all(username)
			for b in l:
				s+=b[0] + "\nPrice: "+ str(b[1])
				
				self.t = tk.Text(self, width=50, height=25)
				self.t.grid(row=12,column=1)
				self.t.insert(tk.END,s)

class Toppings(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.configure(bg='azure')
		tk.Label(self, bg="azure",text='Toppings').grid(row=0, column=1)
		#self.chicken=self.
		# img=open("image/chicken.png")
		# self.chicken=ImageTk.PhotoImage(PIL.Image.open(img))
		# panel=Label(root,image=self.chicken)
		# panel.pack(side="bottom",fill="both",expand="yes")
		# self.bacon=tk.PhotoImage(file="image/bacon.png")
		# self.tomato = tk.PhotoImage(file="image/tomato.png")
		# self.olives = tk.PhotoImage(file="image/olives.png")
		# self.salsa = tk.PhotoImage(file="image/salsa.png")
		# # #self.chicken = Image.open('image/chicken.png')
		# # self.chicken = self.chicken.resize((20, 20))
		# # self.chicken=tk.PhotoImage(self.chicken)
		tk.Label(self, text="Chicken", bg="azure").grid(row=1, column=0)
		tk.Label(self, text="Bacon", bg="azure").grid(row=1, column=1)
		tk.Label(self, text="Tomato", bg="azure").grid(row=1, column=2)
		tk.Label(self, text="Olives", bg="azure").grid(row=4, column=0)
		tk.Label(self, text="Salsa", bg="azure").grid(row=4, column=1)
		tk.Button(self, text="Add",command=lambda: [ls[i].add_ext("Chicken"),self.change_ingre()]).grid(row=2, column=0)
		tk.Button(self, text="Add",command=lambda: [ls[i].add_ext("Bacon"),self.change_ingre()]).grid(row=2, column=1)
		tk.Button(self, text="Add",command=lambda: [ls[i].add_ext("Tomato"),self.change_ingre()]).grid(row=2, column=2)
		tk.Button(self, text="Add",command=lambda: [ls[i].add_ext("Olives"),self.change_ingre()]).grid(row=5, column=0)
		tk.Button(self, text="Add",command=lambda: [ls[i].add_ext("Salsa"),self.change_ingre()]).grid(row=5, column=1)
		tk.Button(self, text="Remove",command=lambda: [ls[i].remove_ext("Chicken"),self.change_ingre()]).grid(row=3, column=0)
		tk.Button(self, text="Remove",command=lambda: [ls[i].remove_ext("Bacon"),self.change_ingre()]).grid(row=3, column=1)
		tk.Button(self, text="Remove",command=lambda: [ls[i].remove_ext("Tomato"),self.change_ingre()]).grid(row=3, column=2)
		tk.Button(self, text="Remove",command=lambda: [ls[i].remove_ext("Olives"),self.change_ingre()]).grid(row=6, column=0)
		tk.Button(self, text="Remove",command=lambda: [ls[i].remove_ext("Salsa"),self.change_ingre()]).grid(row=6, column=1)
		self.warn = tk.Text(self, width=30, height=5)
		self.warn.insert(tk.END, ls[i].get_status())
		self.warn.grid(row=7, column=1)

		tk.Button(self, text="Previous page",command=lambda: master.change_page(MainMenu)).grid(row=8, column=0)
		tk.Button(self, text="Buy",command=lambda: master.change_page(Purchase)).grid(row=8, column=2)
		
	def change_ingre(self):
		self.warn.delete(0.0, tk.END)
		self.warn.insert(tk.END, ls[i].get_status())

class Db_Customer(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self, master)
		self.configure(bg='azure')
		tk.Button(self, text="Previous page",command=lambda: master.change_page(MainMenu)).grid(row=0, column=0)
		tk.Label(self,text = 'Pizza: ',bg="azure",font = ('',20),pady=5,padx=5).grid(row=1,column=0)
		tk.Label(self,text = 'Price: ',bg="azure",font = ('',20),pady=5,padx=5).grid(row=1,column=1)

		l=db_for_customer.getting_all(customer)
		k=2
		for p in l:
			self.te = tk.Text(self,width=40,height=10)
			self.te.grid(row=k, column=0)
			self.te.insert(tk.END, p[0])
			self.te = tk.Text(self,width=10,height=10)
			self.te.grid(row=k, column=1)
			self.te.insert(tk.END, p[1])
			k+=2
			

class Purchase(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)	
		self.configure(bg="azure")
		Label(self,text="Purchase",bg="azure",font = ('',20),pady=5,padx=5).grid(row=0,column=1)
		tk.Button(self, text="Previous page",command=lambda: master.change_page(Toppings)).grid(row=1, column=0)
		p = 0.0
		for i in ls:
			p += i.get_price()
		tk.Button(self, text="Purchase", command=lambda:[db_for_customer.insert(ls, p, customer),master.change_page(MainMenu)]).grid(row=1, column=2)
		tk.Button(self, text="Want more pizza?",command=lambda: [incre(), master.change_page(MainMenu)]).grid(row=2, column=0)
		tk.Button(self, text="Remove the pizza?", width=30,command=lambda: [decre(), self.change_ingre()]).grid(row=2, column=2)
		tk.Label(self, text="Price:", bg='azure').grid(row=4, sticky=tk.W)
		self.res = tk.Text(self)

		self.res.insert(tk.END, "$ " + str(p))
		self.res.grid(row=5)
		tk.Label(self, text="Ingredients:", bg='azure').grid(row=6, sticky=tk.W)
		self.ingre = tk.Text(self,wrap=tk.WORD)
		for j in ls:
			self.ingre.insert(tk.END, '' + j.get_status())
			self.ingre.grid(row=7)

	def change_ingre(self):
		self.res.delete(1.0, tk.END)
		self.ingre.delete(1.0, tk.END)

		p = 0
		for j in ls:
			p += j.get_price()
		self.res.insert(tk.END, "$ " + str(p))
		self.res.grid(row=5)
		tk.Label(self, text="Ingredients:", bg='azure').grid(row=6, sticky=tk.W)
		t = 8
		for j in ls:
			self.ingre = tk.Text(self,wrap=tk.WORD)
			self.ingre.insert(tk.END, j.get_status())
			self.ingre.grid(row=t)
			t=t+1
