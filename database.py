"""
Project     : Inventory Management System
Author      : Aditya Abhishek Tripathi

Database handler for Inventory Management System
"""

import time
import json

class DatabaseHandler:
    def __init__(self, inventory_path, sales_path):
        self.path = inventory_path  # filepath of database
        self.inventory = {}
        self.sales_path = sales_path
        self.sales = {}

    def load_inventory(self):
        """Loads the inventory from database"""
        try:
            with open(self.path, "r") as f:
                self.inventory = json.loads(f.read())
        except FileNotFoundError:
            print("Database Not found")

    def update_inventory(self):
        """Updates any changes in the values of existing product"""
        with open(self.path, "w") as f:
            json.dump(self.inventory, f)

    def transaction_id(self):
        """Generates a unique transaction id for every purchase"""
        try:
            with open("t_id.txt", "r") as f:
                t_id = int(f.read())
        except FileNotFoundError:
            t_id = 0
        finally:
            with open("t_id.txt", "w") as f:
                f.write(str(t_id + 1))
            return t_id
        
    def load_sales(self):
        """loads transaction records from database"""
        try:
            with open(self.sales_path, "r") as f:
                self.sales = json.loads(f.read())
        except FileNotFoundError:
            print("Database Not found")

    def update_sales(self, username, phone, grand_total, bill, t_id):
        """Updates sales after each purchase"""
        self.sales[str(t_id)] = {
            "Username": username,
            "Phone": phone,
            "Grand Total": grand_total,
            "Bill": bill,
            "Purchase Time": time.ctime(),
        }
        with open(self.sales_path, "w") as f:
            json.dump(self.sales, f)