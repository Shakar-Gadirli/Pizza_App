import abc
from Programs import admin_page
class Abstract_Pizza(metaclass = abc.ABCMeta):
	@abc.abstractmethod
	def get_price(self):
		pass

	@abc.abstractmethod
	def get_status(self):
		pass


class PizzaDecorator(Abstract_Pizza):
	def __init__(self,pizza):
		self.pizza=pizza

	def get_price(self):
		return self.pizza.get_price()
	def get_status(self):
		return self.pizza.get_status()

class Tomato(PizzaDecorator):
	def __init__(self,pizza):
		super(Tomato,self).__init__(pizza)
		self.__tomato_price=2
	@property
	def price(self):
		return self.__tomato_price
	def get_price(self):
		return super(Tomato,self).get_price()+self.__tomato_price
	def get_status(self):
		return super(Tomato,self).get_status() + " Tomato"

class Cheese(PizzaDecorator):
	def __init__(self,pizza):
		super(Cheese,self).__init__(pizza)
		self.__cheese_price=3
	@property
	def price(self):
		return self.__cheese_price
	def get_price(self):
		return super(Cheese,self).get_price() + self.__cheese_price

	def get_status(self):
		return super(Cheese,self).get_status() + " Cheese"

class Olives(PizzaDecorator):
	def __init__(self,pizza):
		super(Olives,self).__init__(pizza)
		self.__olives_price=1
	@property
	def price(self):
		return self.__olives_price
	def get_price(self):
		return super(Olives,self).get_price() + self.__olives_price
	def get_status(self):
		return super(Olives,self).get_status() + " Olives"

class Chicken(PizzaDecorator):
	def __init__(self,pizza):
		super(Chicken,self).__init__(pizza)
		self.__chicken_price=4

	@property
	def price(self):
		return self.__chicken_price
	def get_price(self):
		return super(Chicken,self).get_price()+self.__chicken_price
	def get_status(self):
		return super(Chicken,self).get_status() + " Chicken"

class Bacon(PizzaDecorator):
	def __init__(self,pizza):
		super(Bacon,self).__init__(pizza)
		self.__bacon_price=5
	@property
	def price(self):
		return self.__bacon_price
	def get_price(self):
		return super(Bacon,self).get_price() + self.__bacon_price
	def get_status(self):
		return super(Bacon,self).get_status() + " Bacon"

class Salsa(PizzaDecorator):
	def __init__(self,pizza):
		super(Salsa,self).__init__(pizza)
		self.__salsa_price=1
	@property
	def price(self):
		return self.__salsa_price
	def get_price(self):
		return super(Salsa,self).get_price() + self.__salsa_price
	def get_status(self):
		return super(Salsa,self).get_status() + " Salsa"

class Pizza(Abstract_Pizza):

	def __init__(self,name,ingrs,price):
		self.name=name
		self.ingrs=ingrs
		self.price=price
	def get_status(self):
		return self.name+ "\n"+ self.ingrs
	def get_price(self):
		return self.price

class Supreme(Abstract_Pizza):
	__pizza_price=10
	def get_price(self):
		return self.__pizza_price
	def get_status(self):
		return "Supreme:\n Slices Pepperoni, Italian sausage,Chopped onions,Green pepper,Olives"

class Hawaiian(Abstract_Pizza):
	__pizza_price=12
	def get_price(self):
		return self.__pizza_price
	def get_status(self):
		return "Hawaiian:\n Pineapple, Cheese, Ham, Bacon"


class Pizza_Builder:
	def __init__(self,type_of_pizza,row=None):
		self.type_of_pizza=type_of_pizza
		if(type_of_pizza=="Pizza"):
			self.pizza=Pizza(row[0],row[1],row[2])
			self.name=row[0]
			self.ingrs=row[1]
			self.price=row[2]
		else:
			self.pizza=eval(type_of_pizza)()
		self.extentions = []
		
	def add_ext(self,extention):
		self.pizza=eval(extention)(self.pizza)
		self.extentions.append(extention)

	def remove_ext(self,extention):
		if(extention in self.extentions):
			self.extentions.remove(extention)
		if self.type_of_pizza=="Pizza":
			self.pizza = Pizza(self.name, self.ingrs, self.price)
		else:
			self.pizza = eval(self.type_of_pizza)()
		for exten in self.extentions:
			self.pizza= eval(exten)(self.pizza)
	def get_status(self):
		return self.pizza.get_status()
	def get_price(self):
		return self.pizza.get_price()
