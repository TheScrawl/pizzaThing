import os

#Variable Declarations and class definitions
orderType = None
orderPrice = 0
regularList = ['cheese', 'pepperoni', 'sand', 'meat', 'onion', 'bbq sause', 'mayo']
gourmetList = ['unicorn', 'human (adult)', 'human (child)', 'food', 'dog biscuit']
gourmetOrderList = []
regularOrderList = []

class customer(object): 
    def __init__(self, name, address, phoneNum):
        self.name = name
        self.address = address
        self.phoneNum = phoneNum

#Function for getting order Type
def getOrderType(): 
    global orderType
    orderType = None
    print('1: Delivery')
    print('2: Pickup')
	    
    orderType = input()
    try:
        if int(orderType) == 1 or int(orderType) == 2:
	    pass
        else:
            raise ValueError    
    except ValueError:
        orderType = None
        print('invalid option try again')
        getOrderType()
        

def printPizza(): #Function for printing avaliable pizza options
    print('\nStandard Pizzas')
    for index, val in enumerate(regularList):
        print(str(index + 1) + ': ' + str(val))
    print('\nGourmet Pizzas')
    for index, val in enumerate(gourmetList):
        print(str(index + 8) + ': ' + str(val))


def printOrder(): #Function for nicely printing current order so far
    print('Regular Pizzas ($8.50 Each):')
    for i in regularList:
        print(i +  ': ' + str(regularOrderList.count(i)))
    print('\nGourmet Pizzas ($13.50 Each):')
    for i in gourmetList:
        print(i + ': ' + str(gourmetOrderList.count(i)))


def getPizza(): # Main Ordering function
    os.system('clear')
    while True:
	print('Type "n" to end order')
        printPizza()
        pizzaInput = input('Pizza Num: ')
        try:
            if int(pizzaInput) <= 7:
                regularOrderList.append(regularList[int(pizzaInput) - 1])
            if int(pizzaInput) > 7:
                gourmetOrderList.append(gourmetList[int(pizzaInput) - 8])
            os.system('clear')
            printOrder()
        except (ValueError, IndexError):
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
	    print('invalid choice, defaulting to yes')
	    pass
    else:
        pass

#Get Order Type
getOrderType()
if orderType == 1:
    customer1 = customer(
        str(input('Customer Name: ')),
        str(input('Customer Address: ')),
        str(input('Customer Phone Num: '))
)

if orderType == 2:
    customer1 = customer(str(input('Customer Name: ')), None, None)

#Order Pizza
getPizza()
os.system('clear')
#Calculate Order Price
for i in gourmetOrderList:
    orderPrice = orderPrice + 13.50
for i in regularOrderList:
    orderPrice = orderPrice + 8.50
#Final Output
printOrder()
print('\nTotal Cost: ' + str(orderPrice))
print('Name: ' + customer1.name)
print('Address: ' + str(customer1.address))
print('Phone Num: ' + str(customer1.phoneNum))
