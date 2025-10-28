"""# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]"""


# number = 1,2,3,4,5
# for num in number:
#     print(num**2, end=" ")

"""Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
"""

# name_a = []
# names = ["John", "Sara", "Mike", "Amanda"]
# for name in names:
#     if 'a' in name:
#         name_a.append(name)
# print(name_a)

"""
Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
"""

# result = []
# numbers = [5, 12, 3, 18, 7]
# for num in numbers:
#     if num > 10:
#         result.append(True)
#     if num < 10:
#         result.append(False)
# print(result)


"""4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
"""

# last_char = []
# animals = ["dog", "cat", "lion", "tiger"]
# for animal in animals:
#     last_char.append(animal[-1])
# print(last_char)


"""
Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
"""


# numbers = [5, 12, 3, 18, 7]
# print(all(num > 10 for num in numbers))

"""Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
"""

# names = ["John", "Sara", "Mike", "Amanda"]
# print(any('a' in name for name in names))

"""Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
"""

# words = ["HELLO", "world", "pyTHon", "ROCKS"]
# print(any(word.isupper for word in words))


"""
Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
"""

# words = ["apple", "zebra", "mango", "lemon"]
# print(any ('z' in word[0] for word in words))

"""Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
"""

# emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# print(any('org' in email for email in emails))


"""Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
"""

# numbers = [1, 3, 5, 7, 9]
# print(any(num % 2 == 0 in num for num in numbers))


"""Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
"""

# words = ["hi", "dog", "go", "sun"]
# result = all(len(word) > 2 for word in words)
# print(result)

# names = ["John", "Sara", "Mike", "Amanda"]
# names_with_a = [name for name in names if 'a' in name]
# print(names_with_a)


# numbers = [5, 12, 3, 18, 7]
# all_is_greater = []

# for number in

# for i in range (1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# acro = []
# user_input = input("Enter you words: ").title().split()
# for word in user_input:
#     acro.append(word[0])
# print(''.join(acro))

"""Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
Sample Input and Output:
Enter password: hello
Password must be at least 8 characters long and have a maximum of 25 characters.
Enter password: mysecretpasswordisasecret
Password accepted.
"""

while True:
    user_password = input("Enter your password : ")
    password_len = len(user_password)
    if password_len < 8:
        print("Password lengnt must be atleast 8 characters")
    elif password_len > 25:
        print("Password must be between 8 and 25 characters")
    else:
        print("Password accepted")
        break


"""Write a program that asks for the user's age and keeps prompting them until they 
	enter a valid age (greater than or equal to 0).
	Sample Input and Output:
	Enter your age: -5
	Invalid age. Please enter a valid age.
	Enter your age: 25
	Age accepted."""

while True:
    user_age = (int(input("Enter Ayour Age : ")))
    if user_age <= 0:
        print("Invalid Age")
    else:
        print("Age Accepted")
        break

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
inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}

print(text2art("Inventory  Syetem"))

while True:
    print(f"Current Inventory {inventory}")

    operator = input("Enter operation (add/remove/exit): ").lower()

    if operator == "exit":
        print("Thank you for shopping with us! Goodbye")
        break

    item = input("Enter item: ")
    quantity = int(input("Enter quantity: "))

    if operator == "add":
        if item in inventory:
            inventory[item] += quantity
        else:
            if item not in inventory:
                add_operator = input(
                    f"{item} Not Found in item list, Would you like to add {item} to your invetory list? : yes/no : ").lower()
                if add_operator == "yes":
                    inventory[item] = quantity
                    print(f"Added {quantity} {item}")
                else:
                    break

    elif operator == "remove":
        if item in inventory:
            inventory[item] -= quantity
        else:
            if item not in inventory:
                print("f{item} Not Found in item list")

print(inventory)
