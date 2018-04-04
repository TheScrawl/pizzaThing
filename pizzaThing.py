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
		print(str(index + 8) + ': ' + str(val))

def printOrder():
	print('Regular Pizzas ($8.50 Each):')
	for i in regularList:
		print(i +  ': ' + str(regularOrderList.count(i)))
	print()
	print('Gourmet Pizzas ($13.50 Each):')
	for i in gourmetList:
		print(i + ': ' + str(gourmetOrderList.count(i)))

def getPizza():
	os.system('clear')
	print('type "n" to cancel')
	while True:
		printPizza()
		pizzaInput = input('Pizza Num: ')
		try:
			if int(pizzaInput) <= 7:
				regularOrderList.append(regularList[int(pizzaInput) - 1])
			if int(pizzaInput) > 7:
				gourmetOrderList.append(gourmetList[int(pizzaInput) - 8])
			os.system('clear')
			printOrder()			
		except ValueError:
			pass
		except IndexError:
			pass
			
		if len(gourmetOrderList) + len(regularOrderList) >= 5:
			print('You cant order any more')
			break
		if str(pizzaInput) == 'n':
			break

	if len(gourmetOrderList) + len(regularOrderList) < 5:	
		orderMore = input('Order Finished? y/n: ')
		if orderMore == 'y':
			pass
		if orderMore == 'n':
			getPizza()
	else:
		pass

#Get Order Price
getPizza()
os.system('clear')
orderPrice = 0
for i in gourmetOrderList:
	orderPrice = orderPrice + 13.50
for i in regularOrderList:
	orderPrice = orderPrice + 8.50
printOrder()
print()
print('Total Cost: ' + str(orderPrice))
print('Name: ' + customer1.name)
print('Address: ' + str(customer1.address))
print('Phone Num: ' + str(customer1.phoneNum))
