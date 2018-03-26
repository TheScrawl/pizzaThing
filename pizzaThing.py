import os
orderType = None
def getOrderType(): 
	global orderType
	print('1: Delivery')
	print('2: Pickup')
	orderType = int(input())
	if orderType == 1:
		orderType = 'Delivery'
	if orderType == 2:
		orderType = 'Pickup'
	else:
		orderType == None
		pass
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

def printPizza():
	#Print pizza options
	global orderList
	print()
	print('Standard Pizzas')
	for index, val in enumerate(regularList):
		print(str(index + 1) + ': ' + str(val))
	print()
	print('Gourmet Pizzas')
	for index, val in enumerate(gourmetList):
		print(str(index + 1) + ': ' + str(val))
printPizza()

def printOrder():
	print('Regular Pizzas:')
	for i in regularList:
		print(i +  ': ' + str(regularOrderList.count(i)))
	print('Gourmet Pizzas:')
	for i in gourmetList:
		print(i + ': ' + str(gourmetOrderList.count(i)))

def getPizza():
	#get gourmet orders
	gourmetBool = input('Gourmet (y/n)? ')	
	if gourmetBool == 'y':
		print('type "n" to cancel')
		while True:
			pizzaInput = input('Pizza Num: ')
			try:
				gourmetOrderList.append(gourmetList[int(pizzaInput) - 1])
				os.system('clear')
				printOrder()			
			except ValueError:
				pass
			if str(pizzaInput) == 'n':
				break
	#get regular orders
	if gourmetBool == 'n':
		print('type "n" to cancel')
		while True:
			pizzaInput = input('Pizza Num: ')
			try:
				regularOrderList.append(regularListList[int(pizzaInput) - 1])
				os.system('clear')
				printOrder()
			except ValueError:
				pass
			if str(pizzaInput) == 'n':
				break
		
printOrder()
getPizza()	
