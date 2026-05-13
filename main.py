"""
Project     : Inventory Management System
Author      : Aditya Abhishek Tripathi

Main app for Inventory Management System.
"""

from app_utils import App

INVENTORY = "inventory.json"
SALES = "sales.json"

app = App(inventory_path=INVENTORY, sales_path=SALES)
cmd_list = {
    "buy": app.buy,
    "cart": app.show_cart,
    "end": app.end,
    "help": app.cmd_help,
    "shop": app.shop,
    "new": app.customer_details
}  # This consists of commands which don't require a parameter

app.customer_details()
app.welcome_screen()
print("Type help for a list of available commands.")

while True:
    print("*" * 20)
    cmd = input("Enter the command: ")
    print("*" * 20)
    try:
        cmd_list[cmd]()
    except KeyError:
        if cmd.startswith("cart add "):
            qty = int(cmd.split()[2])
            id = cmd.split()[3]
            app.cart_add(qty, id)
        elif cmd.startswith("cart remove "):
            id = cmd.split()[2]
            app.cart_remove(id)
        elif cmd.startswith("show "):
            t_id = str(cmd.split()[1])
            app.show_details(t_id)
        else:
            print("Invalid Command")