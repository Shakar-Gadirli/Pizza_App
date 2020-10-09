import sqlite3



def create(username):
	try:
		c = sqlite3.connect('Customer_DB.db')
		cur=c.cursor()
		m_q=f"CREATE TABLE {username} (pizza TEXT, price REAL)"
		cur.execute(m_q)
		c.commit()
		cur.close()
	except sqlite3.Error as error:
		print(error)
	finally:
		if(c):
			c.close()

def insert(ls,price,username):
	st=""
	for p in ls:
		st=st+p.get_status() + '\n'
	try:
		c=sqlite3.connect("Customer_DB.db")
		cur=c.cursor()
		i_q=f"INSERT INTO {username} (pizza,price) VALUES(?,?)"
		cur.execute(i_q,(st,price))
		c.commit()
		cur.close
	except sqlite3.Error as error:
		print(error)
	finally:
		if(c):
			c.close()
def getting_all(username):
	try:
		c=sqlite3.connect("Customer_DB.db")
		cur=c.cursor()
		s_q=f"SELECT * FROM {username}"
		cur.execute(s_q)
		return cur.fetchall()
		cur.close()
	except sqlite3.Error as error:
		print(error)
	finally:
		if (c):
			c.close()
def look_for(username):
	try:
		c = sqlite3.connect("Customer_DB.db")
		cur = c.cursor()
		q = f"SELECT * FROM {username}"
		cur.execute(q)
		return cur.fetchall()
		cur.close()

	except sqlite3.Error as error:
		print(error)

	finally:
		if(c):
			c.close()
