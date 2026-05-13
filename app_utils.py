"""
Project     : Inventory Management System
Author      : Aditya Abhishek Tripathi

UI/UX handler for Inventory Management System.
"""

from database import DatabaseHandler
import json

class App(DatabaseHandler):
    """This class handles the frontend and backend functionalities of Inventory Management System"""
    
    def __init__(self, inventory_path, sales_path):
        super().__init__(inventory_path, sales_path)  # Connects app to database
        self.username = ""
        self.phone = ""
        self.cart = {} # "Product ID": {"Product Name": ---, "Quantity": ---, "Price": ---}

    def welcome_screen(self):
        """Display welcome message to user when app starts and loads the data from file"""
        print("Inventory Management System")
        print("Connecting to database...")
        try:
            self.load_inventory()
            self.load_sales()
        except json.decoder.JSONDecodeError:
            pass

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
        print("new                      : Begins purchase for a new customer")
        print("show <transaction_id>    : Shows transaction details for a previous purchase")

    def customer_details(self):
        self.username = input("Enter your name: ")
        self.phone = input("Enter your phone number: ")

    def generate_bill(self):
        """Generates and prints the bill for items in cart"""
        gt = 0  # GRAND_TOTAL
        bill = "-"*20+"\n"
        for id in self.cart.keys():
            total = self.cart[id]["Quantity"]*self.cart[id]["Price"]
            gt += total
            bill += f"ID: {id}\nName: {self.cart[id]["Product Name"]}\nQuantity: {self.cart[id]["Quantity"]}\nPrice: {self.cart[id]["Price"]}\nTotal: {total}\n"+"-"*20+"\n"

        return bill, gt

    def buy(self):
        """Purchase items in cart"""
        if self.cart:
            bill, gt = self.generate_bill()
            print(bill)
            print(f"GRAND TOTAL: {gt}")
            cnf = ""
            while cnf.lower() != 'y':
                cnf = input("Confirm purchase? (y/n) : ")
                if cnf.lower() == 'n':
                    return None # User continues to buy if choses n else prompted for confirm choice each time
            for id in self.cart.keys():
                self.inventory[id]["Quantity"] -= self.cart[id]["Quantity"] # update inventory in program
            self.cart.clear()    # empty the cart for next purchase
            self.update_inventory() # update the inventory after purchase is confirmed
            print("Purchase Successful")
            t_id = self.transaction_id()
            print(f"Transaction id: {t_id}")
            self.update_sales(self.username, self.phone, gt, bill, t_id)
        else:
            print("No items in cart.")

    def show_details(self, t_id):
        if t_id in self.sales.keys():
            print(f"TRANSACTION ID\n{t_id}\n")
            for detail in self.sales[t_id].keys():
                print(f"{detail.upper()}\n{self.sales[t_id][detail]}\n")
        else:
            print(f"Invalid Transaction ID {t_id}")

# Cart functionalities

    def show_cart(self):
        """Display items in cart"""
        if self.cart:
            print("Cart")         
            bill, gt = self.generate_bill()
            print(bill)
            print(f"GRAND TOTAL: {gt}")
        else:
            print("Cart is Empty")

    def cart_add(self, qty, id):
        """Add items to cart"""
        try:
            if qty <= self.inventory[id]["Quantity"]:    
                self.cart[id] = {"Product Name": self.inventory[id]["Product Name"], "Quantity": qty, "Price": self.inventory[id]["Price"]}
                print(f"{qty} units of {self.inventory[id]["Product Name"]} added to cart")
            else:
                print(f"Only {self.inventory[id]["Quantity"]} units of {self.inventory[id]["Product Name"]} are available")
        except KeyError:
            print(f"Invalid Product id {id}")            

    def cart_remove(self, id):
        """Remove items from cart"""
        try:
            del self.cart[id]
            print(f"{self.inventory[id]["Product Name"]} removed from cart")
        except KeyError:
            print(f"Invalid product ID {id}")

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
        for id in self.inventory.keys():
            print(f"ID: {id}")
            print(f"Name: {self.inventory[id]["Product Name"]}")
            print(f"Quantity: {self.inventory[id]["Quantity"]}")
            print(f"Price: {self.inventory[id]["Price"]}")
            print("-"*20)