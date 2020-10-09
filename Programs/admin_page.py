import sqlite3
from Programs import db_for_customer
from Programs import login_page

def create():
	try:
		c=sqlite3.connect("pizzas.db")
		cur=c.cursor()
		cur.execute("""CREATE TABLE pizzas (name TEXT, status TEXT,price REAL)""")
		c.commit()
		cur.close()
	except sqlite3.Error as error:
		pass
	finally:
		if(c):
			c.close()
create()
def look_for(username):
	customer=login_page.search(username)
	info=db_for_customer.look_for(username)
def add_pizza(name,status,price):
	try:
		c=sqlite3.connect("pizzas.db")
		cur=c.cursor()
		
		cur.execute('SELECT * FROM pizzas WHERE name = ?',(name,))
		r=cur.fetchone()
		if name!="Supreme" and name!="Hawaiian" and not r:
			send="""INSERT INTO pizzas (name,status,price) VALUES (?,?,?)"""
			cur.execute(send,(name,status,price))
			c.commit()
			file=open("Programs/notifications.txt","w+")
			file.write(f"Hey! See new {name} pizza")
			file.close()
			return "You added pizza"
		else:
			return "This Pizza exists!"
		cur.close()
	except sqlite3.Error as error:
		print(error)
	finally:
		if(c):
			c.close()


def choose_a_data(username):
	try:
		c=sqlite3.connect("pizzas.db")
		cur=c.cursor()	
		cur.execute('SELECT * FROM pizzas WHERE name = ?',(username,))
		return cur.fetchall()
		cur.close()
	except sqlite3.Error as error:
		print(error)
	finally:
		if(c):
			c.close()
def choose_all_data():
	try:
		c=sqlite3.connect("pizzas.db")
		cur=c.cursor()	
		cur.execute('SELECT * FROM pizzas ')
		return cur.fetchall()
		cur.close()
	except sqlite3.Error as error:
		print(error)
	finally:
		if(c):
			c.close()




