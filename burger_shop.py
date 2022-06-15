# implement the classes listed below 
class FoodItem:
    name = ""
    
    def __init__(self,name):
        self.name = name
        
    def display(self):
        return self.name

class Burger(FoodItem):
    
    burger_price = {
    'chicken':5,
    'beef':6,
    'veggie':4
    }
 
    def __init__(self,name):
        self.name = name
    
    def get_price(self):
        return self.burger_price.get(self.name)
    
    def display(self):
        print("Burger selection: ", self.name)
        print("price: ", self.get_price())
        
class Drink(FoodItem):
    size = ""           #small, medium, or large
    
    drink_price = {
    'cola':5,
    'orange juice':6,
    'water':4
    }
    
    def __init__(self,name,size):
        self.name = name
        self.size = size
        
    def get_price(self):
        return self.drink_price.get(self.name)
    
    def display(self):
        print("Drink selection: ", self.drink_type)
        print("Drink size: ", self.size)
        print("price: ", self.get_price())


'''

class Side(FoodItem):
    #fries or salad
    pass
class Combo(FoodItem):
    pass

''' 
class Order:
    name = ""
    items = list()
    total = 0
    
    def __init__(self,name):
        self.name = name
        
    def add_item(self, item):
        self.items.append(item)
        
    def total_cost(self):
        for item in self.items:
   
            price = item.get_price()
            self.total+=price
        return self.total
            
        
    def display(self):
        for x in range(0,len(self.items)):
            print("Item %d: %s"%(x, self.items[x].name))
        self.total_cost() #calculates the cost of all orders
        print("Your total cost is: ", f"${self.total:.2f}")
    pass
 
def user_input_burger():
    #ask user for input and store it in burger object 
    burger_type = input("Chicken, beef, or veggie? ").lower()

    b = Burger(burger_type)

    return b

def user_input_drink():
    #ask user for input and store it in drink object 
    drink_type = input("Cola, Orange Juice, or Water? ").lower()
    size = input("Small, medium, or large? ").lower()
    d = Drink(drink_type,size)
    return d
''' 
def user_input_side():
    s = Side()
    #ask user for input and store it in side object 
    return s
 
def user_input_combo():
    c = Combo()
    #ask user for input and store it in combo object 
    #a combo must include one burger, one side, and one drink
    return c
 '''
def take_order():
    #ask user for name for the order 
    #repeat taking order until client is done 
    #display order details
    #display a thank you message
    print("Welcome to Burger Shop")
    
    total_price=0
    orderStr="You ordered a "
    price = dict()
    
    

    print("---------------------------------------------------")
    

    user_name = input("Please enter you name: ").upper()
    order = Order(user_name)

    while True:

        quit=input("Type 1 to add a new item or any other key to quit. ")

        if quit != '1':
            break
        
        item = input("Would you like a burger, a side, a drink or a combo? ").lower()
        
        if item == "burger":
            item = user_input_burger()
            order.add_item(item)
        elif item == 'drink':
            item = user_input_drink()
            order.add_item(item)
        else:
            print("Not a valid item!")

    
    print()
    print("            THANK YOU FOR YOUR ORDER", order.name)
    print("---------------------------------------------------")
    print("----------------Your Order Summary-----------------")
    print("---------------------------------------------------")
    order.display()


take_order()
