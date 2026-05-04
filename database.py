"""
Project     : Inventory Management System
Author      : Aditya Abhishek Tripathi

Database handler for Inventory Management System
"""

import time


class DatabaseHandler:
    def __init__(self, inventory_path, sales_path):
        self.path = inventory_path  # filepath of database
        self.inventory = {
            "id": [],
            "name": [],
            "qty": [],
            "price": [],
        }  # handles inventory updates
        self.sales_path = sales_path

    def load_inventory(self):
        """Loads the content from database"""
        try:
            f = open(self.path, "r")
        except FileNotFoundError:
            print("Database not found")
        else:
            data = f.read()
            f.close()
            products = data.split("\n")  # list of products
            self.inventory["id"] = [
                product.split(",")[0] for product in products
            ]  # id field for products
            self.inventory["name"] = [
                product.split(",")[1] for product in products
            ]  # name field for products
            self.inventory["qty"] = [
                int(product.split(",")[2]) for product in products
            ]  # qty field for products
            self.inventory["price"] = [
                int(product.split(",")[3]) for product in products
            ]  # price field for products
            print("Connection Successful")

    def update_inventory(self):
        """Updates any changes in the values of existing product"""
        txt = ""  # stores raw string to be dumped into file
        for n in range(
            len(self.inventory["id"])
        ):  # updates txt in format id,name,qty,price
            txt += f"{self.inventory["id"][n]},{self.inventory["name"][n]},{self.inventory["qty"][n]},{self.inventory["price"][n]}\n"
        txt = txt[: len(txt) - 1]  # removes last \n
        with open(self.path, "w") as f:
            f.write(txt)

    def update_sales(self, username, phone, grand_total, bill):
            """Updates sales.txt after each purchase"""
            sales_log = (
                f"Username: {username}\nPhone: {phone}\nGrand Total: {grand_total}\nPurchase-time: {time.ctime()}"
                + f"\n{bill}\n"
                + "*" * 20
                + "\n"
            )
            with open(self.sales_path, "a") as f:
                f.write(sales_log)