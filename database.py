"""
Project     : Inventory Management System
Author      : Aditya Abhishek Tripathi

Database handler for Inventory Management System
"""

class InventoryFile:
    def __init__(self, path):
        self.path = path    # filepath of database
        self.inventory = {"id": [], "name": [], "qty": [], "price": []} # handles inventory updates

    def load_inventory(self):
        """Loads the content from database"""
        try:
            f = open(self.path, "r")
        except FileNotFoundError:
            print("Database not found")
        else:
            data = f.read()
            f.close()
            products = data.split("\n") # list of products
            self.inventory["id"] = [product.split(",")[0] for product in products]      # id field for products
            self.inventory["name"] = [product.split(",")[1] for product in products]    # name field for products
            self.inventory["qty"] = [int(product.split(",")[2]) for product in products]     # qty field for products
            self.inventory["price"] = [int(product.split(",")[3]) for product in products]   # price field for products
            print("Connection Successful")

    def update_inventory(self):
        """Updates any changes in the values of existing product"""
        f = open(self.path, "w")
        txt = ""    # stores raw string to be dumped into file
        for n in range(len(self.inventory["id"])):  # updates txt in format id,name,qty,price
            txt += f"{self.inventory["id"][n]},{self.inventory["name"][n]},{self.inventory["qty"][n]},{self.inventory["price"][n]}\n"
        txt = txt[:len(txt)-1]  # removes last \n
        f.write(txt)
        f.close()