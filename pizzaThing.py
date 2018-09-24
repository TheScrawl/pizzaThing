import os

#Variable Declarations and class definitions
orderType = None #Variable for wether its a delivery or pickup  
orderPrice = 0 #Variable for how much the order costs
#Lists of pizzas - changing this list would allow for easy editing of the menu, so long as the number of items remains consistent
regularList = ['cheese', 'pepperoni', 'sand', 'meat', 'onion', 'bbq sause', 'mayo'] 
gourmetList = ['unicorn', 'human (adult)', 'human (child)', 'food', 'dog biscuit']
#Lists to store what the customer has ordered
gourmetOrderList = []
regularOrderList = []

#Customer class, allows for easy creation and storage of data about the customer
class customer(object):
    def __init__(self, name, address, phoneNum):
        self.name = name
        self.address = address
        self.phoneNum = phoneNum

#Function for getting order Type
def getOrderType(): 
    #Get orderType into the local space
    global orderType
    orderType = None
    print('1: Delivery') #Print onscreen info
    print('2: Pickup')
            
    #Take user input
    orderType = input()
    try: #check if ordertype is a valid input (1 or 2), then continue
        if int(orderType) == 1 or int(orderType) == 2:
            pass
        else:
            raise ValueError    
    except ValueError: #If the input is not valid, reset the variable, tell the user off, and restart the function
        orderType = None
        print('invalid option try again')
        getOrderType()
        

def printPizza(): #Function for printing avaliable pizza options
    print('\nStandard Pizzas')
    for index, val in enumerate(regularList): #For each regular pizza, print an associated number and its name
        print(str(index + 1) + ': ' + str(val))
    print('\nGourmet Pizzas')
    for index, val in enumerate(gourmetList): #For each gourmet pizza, print an associated number and its name
        print(str(index + 8) + ': ' + str(val))


def printOrder(): #Function for nicely printing current order so far
    print('Regular Pizzas ($8.50 Each):') #print what pizzas the user has ordered, and the amount
    for i in regularList:
        print(i +  ': ' + str(regularOrderList.count(i)))
    print('\nGourmet Pizzas ($13.50 Each):')
    for i in gourmetList:
        print(i + ': ' + str(gourmetOrderList.count(i)))


def getPizza(): # Main Ordering function
    os.system('clear') #Clear the screen
    while True: #loop this code
        print('Type "n" to end order') #make user aware of how to end the order
        printPizza() #print avaliable pizza and their numbers
        pizzaInput = input('Pizza Num: ') #take user input
        try:
            #check if regular or gorumet
            if int(pizzaInput) <= 7: 
                regularOrderList.append(regularList[int(pizzaInput) - 1]) #add assocated number's pizza to the regular order list
            if int(pizzaInput) > 7:
                gourmetOrderList.append(gourmetList[int(pizzaInput) - 8]) #add assocated number's pizza to the gorumet order list
            os.system('clear')
            printOrder() #Print what has been ordered so far
        except (ValueError, IndexError): #if the nunmber is out of range, ignore that input
            pass
        
        #If the orders reach 5 total pizzas, break the loop and continue to next phase
        if len(gourmetOrderList) + len(regularOrderList) >= 5:
            print('You cant order any more')
            break
        if str(pizzaInput) == 'n':
            break
            
    #Check if order is done
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
getOrderType() #check if delivery or pickup
if int(orderType) == 1: #if the order is a delivery, get full customer detail
    customer1 = customer(
        str(input('Customer Name: ')),
        str(input('Customer Address: ')),
        str(input('Customer Phone Num: '))
)

if int(orderType) == 2: #If the order is a delivery, just get the customer's name
    customer1 = customer(str(input('Customer Name: ')), None, None)

#Order Pizza
getPizza() #Run the main function
os.system('clear') #clean the screen for readability
#Calculate Order Price
for i in gourmetOrderList: #for each gorumet pizza, add 13.50 to the order price
    orderPrice = orderPrice + 13.50
for i in regularOrderList: #for each regular pizza add 8.50 to the order price
    orderPrice = orderPrice + 8.50
#Final Output
printOrder() #print what pizzas were ordered
print('\nTotal Cost: ' + str(orderPrice)) #print final price
#print customer data
print('Name: ' + customer1.name)
print('Address: ' + str(customer1.address))
print('Phone Num: ' + str(customer1.phoneNum))
