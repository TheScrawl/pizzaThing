import os
orderType = None
def getOrderType(): 
	global orderType
	orderType = None
	print('1: Delivery')
	print('2: Pickup')
	
	orderType = input()
	try:
		if int(orderType) == 1:
			orderType = 'Delivery'
		elif int(orderType) == 2:
			orderType = 'Pickup'
		else:
			orderType = None
			print('invalid option try again')
			getOrderType()	
	except ValueError:
		orderType = None
		print('invalid option try again')
		getOrderType()
getOrderType()

class customer(object): 
	def __init__(self, name, address, phoneNum):
		self.name = name
		self.address = address
		self.phoneNum = phoneNum
		

if orderType == 'Delivery':
	customer1 = customer(
		str(input('Customer Name: ')),
		str(input('Customer Address: ')),
		str(input('Customer Phone Num: '))
)

if orderType == 'Pickup':
	customer1 = customer(str(input('Customer Name: ')), None, None)

regularList = ['cheese', 'pepperoni', 'sand', 'meat', 'onion', 'bbq sause', 'mayo']
gourmetList = ['unicorn', 'human (adult)', 'human (child)', 'food', 'dog biscuit']
gourmetOrderList = []
regularOrderList = []

def printPizza(pizzaType):
	#Print pizza options
	global orderList
	if pizzaType == 'regular':
		print()
		print('Standard Pizzas')
		for index, val in enumerate(regularList):
			print(str(index + 1) + ': ' + str(val))
	if pizzaType == 'gourmet':
		print()
		print('Gourmet Pizzas')
		for index, val in enumerate(gourmetList):
			print(str(index + 1) + ': ' + str(val))

def printOrder():
	print('Regular Pizzas:')
	for i in regularList:
		print(i +  ': ' + str(regularOrderList.count(i)))
	print()
	print('Gourmet Pizzas:')
	for i in gourmetList:
		print(i + ': ' + str(gourmetOrderList.count(i)))

def getPizza():
	#get gourmet orders
	os.system('clear')
	printPizza('regular')
	printPizza('gourmet')
	print()
	gourmetBool = input('Gourmet (y/n)? ')	
	if gourmetBool == 'y':
		os.system('clear')
		printPizza('gourmet')
		print('type "n" to cancel')
		while True:
			pizzaInput = input('Pizza Num: ')
			try:
				gourmetOrderList.append(gourmetList[int(pizzaInput) - 1])
				os.system('clear')
				printPizza('gourmet')
				print()
				printOrder()			
			except ValueError:
				pass
			except IndexError:
				pass
			if str(pizzaInput) == 'n':
				break
	#get regular orders
	if gourmetBool == 'n':
		os.system('clear')
		printPizza('regular')
		print('type "n" to cancel')
		while True:
			pizzaInput = input('Pizza Num: ')
			try:
				regularOrderList.append(regularList[int(pizzaInput) - 1])
				os.system('clear')
				printPizza('regular')
				print()
				printOrder()
			except ValueError:
				pass
			except IndexError:
				pass
			if str(pizzaInput) == 'n':
				break
		
printOrder()
getPizza()	
