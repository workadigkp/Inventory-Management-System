"""
Project     : Inventory Management System
Author      : Aditya Abhishek Tripathi

Main app for Inventory Management System.
"""

from app_utils import App

FILE_PATH = "inventory.txt"

app = App(FILE_PATH)
cmd_list = {
    "buy": app.buy,
    "cart": app.show_cart,
    "end": app.end,
    "help": app.cmd_help,
    "shop": app.shop,
}   # This consists of commands which don't require a parameter


app.welcome_screen()
print("Type help for a list of available commands.")

while True:
    cmd = input("Enter the command: ")
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
