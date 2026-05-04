"""
Project     : Inventory Management System
Author      : Aditya Abhishek Tripathi

Main app for Inventory Management System.
"""

from app_utils import App

INVENTORY = "inventory.txt"
SALES = "sales.txt"

username = input("Enter your name: ")
phone = input("Enter your phone number: ")

app = App(inventory_path=INVENTORY, sales_path=SALES, username=username, phone=phone)
cmd_list = {
    "buy": app.buy,
    "cart": app.show_cart,
    "end": app.end,
    "help": app.cmd_help,
    "shop": app.shop,
}  # This consists of commands which don't require a parameter


app.welcome_screen()
print("Type help for a list of available commands.")

while True:
    print("*" * 20)
    cmd = input("Enter the command: ")
    print("*" * 20)
    try:
        cmd_list[cmd]()
    except KeyError:
        if cmd in cmd_list.keys():
            print("Invalid command")
            continue
        elif cmd.startswith("cart add"):
            qty = int(cmd.split()[2])
            id = cmd.split()[3]
            app.cart_add(qty, id)
        elif cmd.startswith("cart remove"):
            id = cmd.split()[2]
            app.cart_remove(id)
            i = app.inventory["id"].index(id)
            print(f"{app.inventory["name"][i]} removed from cart")
