class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """
        The function __init__() is a special function in Python classes. It is run as soon as an object
        of a class is instantiated. The method is useful to do any initialization you want to do with
        your object
        
        :param country: The country where the order was made
        :param code: The code of the product
        :param product: The name of the product
        :param cost: The cost of the product in the country
        :param quantity: The number of items sold
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
       
    def get_cost(self):
        """
        The function get_cost() returns the cost of the item
        :return: The cost of the item.
        """
        return self.cost
    
    def get_quantity(self):
        """
        It returns the quantity of the item.
        :return: The quantity of the item.
        """
        return self.quantity

    def __str__(self):
        """
        The function takes in an object of the class and returns a string representation of the object
        :return: The country, code, product, cost, and quantity.
        """
        return "Country: "+ self.country +", " + "code: "+ self.code + ", "+ "product: "+ self.product+", "+ "cost: "+ str(self.cost) +", "+ "quatity: "+ str(self.quantity)
        

# Shoe_list is a list that stores the objects of the class Shoe.
shoe_list = []

def read_shoes_data():
    """
    This function reads the data from the inventory.txt file and stores it in the shoe_list list
    """
    try:
        count = 0
        with open("inventory.txt", "r") as f:
            for line in f:
                if count != 0:
                    (country, code, product, cost, quantity) = line.rstrip('\n').strip().split(',')
                    shoe_list.append(Shoe(country,code,product,int(cost), int(quantity)))
                count += 1
        print("Data successively stored from inventory.txt")
    except IOError:
        print("The requested file inventory.txt cannot be used")
    
    
def capture_shoes():
    """
    It asks the user for input, then creates a Shoe object with that input, and then appends that object
    to the shoe_list.
    """
    shoes_country = input("Enter the country: ")
    shoes_code = input("Enter the code: ")
    shoes_product = input("Enter the product name: ")
    shoes_cost = int(input("Whats the cost: "))
    shoes_quantity = int(input("Enter Quantity: "))

    shoes = Shoe(shoes_country, shoes_code, shoes_product, shoes_cost, shoes_quantity)
    shoe_list.append(shoes)
    
    

def view_all():
    """
    This function prints out all the shoes in the shoe_list.
    """
    for shoes in shoe_list:
        print(str(shoes))
    
    

def re_stock():
    """
    It takes the first item in the list and compares it to the rest of the items in the list. If it
    finds an item with a lower quantity, it sets that item as the new low stock item
    """
    low_stock = shoe_list[0]
    for shoes in shoe_list:
        if shoes.get_quantity() < low_stock.get_quantity():
            low_stock = shoes
    print("Shoes that are low in stock\n"+str(low_stock))
    should_you_restock = input("Would you like to restock (Yes/No): ").lower()
    if should_you_restock == "yes":
        update_stock = int(input("How many would like to restock: "))
        low_stock.quantity = low_stock.get_quantity() + update_stock
    else:
        print("Thanks for confirming not to restock")
    
    

def search_shoe(code):
    """
    It loops through the list of shoes and returns the shoe object that matches the code
    
    :param code: the code of the shoe
    :return: The shoes object
    """
    for shoes in shoe_list:
        if shoes.code == code:
            return shoes
    
    

def value_per_item():
    """
    This function will print out the total value of each shoe in the shoe list
    :return: The total value of the shoes.
    """
    shoe_value = 0
    for shoes in shoe_list:
        shoe_value = shoes.get_cost() * shoes.get_quantity()
        print(str(shoes) +"\tTotal Value: "+ str(shoe_value))
    return shoe_value
    
   

def highest_qty():
    """
    It loops through the list of shoes and compares the quantity of each shoe to the quantity of the
    first shoe in the list. If the quantity of the shoe being compared is greater than the quantity of
    the first shoe, the shoe being compared is set as the new high stock shoe
    """
    high_stock = shoe_list[0]
    for shoes in shoe_list:
        if shoes.get_quantity() > high_stock.get_quantity():
            high_stock = shoes
    print(str(high_stock))
    
    



def main():# A menu that the user can choose from.
    user_message = '''
    Hello, welcome to Nike store room, please choose one of the options below to proceed:
    A: Read shoes data 
    B: Capture shoes
    C: View all shoes
    D: Restock shoes
    E: Search shoes
    F: Calculate the total value
    G: Exit 
    Enter your option: '''
    
    user_choice = ""
    
    
    while True:
        user_choice = input(user_message).lower()
        if user_choice == "a":
            read_shoes_data()
        elif user_choice == "b":
            capture_shoes()
        elif user_choice == "c":
            view_all()
        elif user_choice == "d":
            re_stock()
        elif user_choice == "e":
            code = input("Enter the code of the shoe you are looking for: ")
            print(str(search_shoe(code)))
        elif user_choice == "f":
            value_per_item()
        elif user_choice == "g":
            print("Thank you for using the program")
            break
        else:
            print("Invalid option, please try again")
main()
