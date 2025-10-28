"""Write a program that tracks the inventory of items in a store. The user should be able 
	to add or remove items and the program should display the current inventory after each
	operation. The program stops when the user decides to exit.
	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
	Sample Input and Output:
	Enter operation (add/remove/exit): add
Enter item: eggs
Enter quantity: 10
Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
Enter operation (add/remove/exit): remove
Enter item: fish
Enter quantity: 50
Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
Enter operation (add/remove/exit): exit
"""

from art import text2art

inventory = {'eggs': 40, 'fish': 150, 'bread': 343, 'yam': 2}
print(text2art("Inventory Syetem"))

while True:
    print(f'Your current inventory is {inventory}')

    operator = input("Enter your Operator (add/remove/exit)").lower()
    if operator == "exit":
        print("Thank you for shopping with us! Goodbye")
        break

    item = input("Enter Item : ")
    quantity = int(input("Enter Quantity : "))

    if operator == "add":
        if item in inventory:
            inventory[item] += quantity
        else:
            if item not in inventory:
                add_operator = input((f'{item} not in inventory, Would you like to add {item} to your inventory? (yes/no)'))
                if add_operator == "yes":
                    inventory[item] = quantity
                    print(f"{item} added")
                else:
                    break
    else:
        if operator == "remove":
            if item in inventory:
                inventory[item] -= quantity
            else:
                print(f"{item} not Found in The List")

print(inventory)

