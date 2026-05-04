"""
Project     : Inventory Management System
Author      : Aditya Abhishek Tripathi

UI/UX handler for Inventory Management System.
"""

from database import InventoryFile

class App(InventoryFile):
    def __init__(self, path):
        super().__init__(path)  # Connects app to database
        self.cart = [] # list of tuple -> (id, name, price, qty)

    def welcome_screen(self):
        """Display welcome message to user when app starts and loads the data from file"""
        print("Inventory Management System")
        print("Connecting to database...")
        self.load_inventory()   # loads data from inventory.txt to program

    def cmd_help(self):
        """Display a list of commands (lexiographical order) for user to interact with app"""
        print("Commands are case sensitive")
        print("buy                      : Purchases all items in cart")
        print("cart                     : Display cart")
        print("cart add <qty> <id>      : Adds <qty> items of product <id> to cart")
        print("cart remove <id>         : Removes items of product <id> from cart")
        print("end                      : Exit the program")
        print("help                     : Prints this list of commands")
        print("shop                     : Displays details of available products")

    def generate_bill(self):
        """Generates and prints the bill for items in cart"""
        gt = 0  # GRAND_TOTAL
        print("-"*20)
        for id, name, price, qty in self.cart:
            total = price*qty
            gt += total
            print(f"ID: {id}")
            print(f"Name: {name}")
            print(f"Quantity: {qty}")
            print(f"Price: {price}")
            print(f"Total: {total}")
            print("-"*20)
        print(f"GRAND_TOTAL = {gt}")

    def buy(self):
        """Purchase items in cart"""
        if self.cart:
            self.generate_bill()
            cnf = ""
            while cnf.lower() != 'y':
                cnf = input("Confirm purchase? (y/n) : ")
                if cnf.lower() == 'n':
                    return None # User continues to buy if choses n else prompted for confirm choice each time
            for product in self.cart:
                self.inventory["qty"][self.inventory["id"].index(product[0])] -= product[3] # update inventory in program
            del self.cart[:]    # empty the cart for next purchase
            self.update_inventory() # update the inventory after purchase is confirmed
            print("Purchase Successful")
        else:
            print("No items in cart.")

    def show_cart(self):
        """Display items in cart"""
        if self.cart:
            print("Cart")         
            self.generate_bill()
        else:
            print("Cart is Empty")

    def cart_add(self, qty, id):
        """Add items to cart"""
        try:
            i = self.inventory["id"].index(id)  # getting index from ID to fetch other details of product
        except ValueError:
            print(f"Invalid Product id {id}")
        else:
            if qty <= self.inventory["qty"][i]:    
                self.cart.append((id, self.inventory["name"][i], self.inventory["price"][i], qty))  # Adding product details to cart
                print(f"{qty} units of {self.inventory["name"][i]} added to cart")
            else:
                print(f"Only {self.inventory["qty"][i]} units of {self.inventory["name"][i]} are available")

    def cart_remove(self, id):
        """Remove items from cart"""
        try:
            i = [p[0] for p in self.cart].index(id)
        except ValueError:
            print(f"Invalid product ID {id}")
        else:
            del self.cart[i]

    def end(self):  
        """Autosaves the last updated inventory and ends the program"""
        print("Autosaving the content...")
        self.update_inventory()
        print("Database Closed")
        print("Thanks for using")
        exit()

    def shop(self):
        """Displays details of available products"""
        print("Shop items")
        print("-"*20)
        for n in range(len(self.inventory["id"])):
            print(f"ID: {self.inventory["id"][n]}")
            print(f"Name: {self.inventory["name"][n]}")
            print(f"Quantity: {self.inventory["qty"][n]}")
            print(f"Price: {self.inventory["price"][n]}")
            print("-"*20)