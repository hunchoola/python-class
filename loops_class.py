# WRite a program that asks the user for input of cities for 10 times and then print out all those cities in a list

# Tell if a number is even
# Tell if it is odd
# tell if a number is a multiple of another
# Prime number


# num = 170

# i = 2

# while i <= num - 1:

#     if num % i == 0:
#         print("Number is not prime")
#         break
   
#     i += 1

# else:
#     print("It is prime.")

# Write a program that accepts a number from the user, tells us if the number is even/odd and also tells us if that number is a prime number


# A simple guess game program that allows the user to guess 5 times and then if they guess correctly, we add to their score

# from random import randint

# score = 0

# i = 0
# while i < 5:
#     c_num = randint(1, 10)
#     print(f"HInt: between {c_num + 2} and {c_num - 2}")


#     u_num = int(input('Enter your guess (between 1-10): '))

#     if c_num == u_num:
#         score += 5
#         print(f"Correct guess. You have scored {score}")
#         # break
#     else:
#         print("Incorrect guess.")

#     i += 1

# print(f"Total score: {score}")




# For loops

# for i in range(6): # 0, 1, 2, 3, 4, 5
#     print("My name is Tobi")


# Write a program that uses a for loop to just accept a user's name 16 times
# for i in range(1, 17):
#     name = input("Enter your name: ")
#     print(f"The name you supplied is : {name}")


# A program that asks the user to provide two numbers every time for 8 times and then every single time, raise the first number the power of the second number

# for i in range(8):
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))

#     print(num1 ** num2)


# Can you build a multiplication table using a for loop?

# table = 3


# for i in range(1, 13):
#     print(f"{table} x {i} = {table * i} ")


# animals = ["Hippo", "Elephant", "Cheetah", "Falcon", "Eagle", "Leopard", "Jaguar"]

# for i in range(len(animals)):
#     print(animals[i])


# students = [
#     ['Tobi', 'E0038882'],
#     ['John', "16/88238"],
#     ['Bryce', "883/882"]
# ]

# for i in range(len(students)):
#     print(students[i][1])




# animals = ["Hippo", "Elephant", "Cheetah", "Falcon", "Eagle", "Leopard", "Jaguar"]

# for i in range(3, len(animals) - 1):
#     print(animals[i])



# animals = ["Hippo", "Elephant", "Cheetah", "Falcon", "Eagle", "Leopard", "Jaguar"]
# for i in range(len(animals)):
#     print(animals[i][-1])

# for i in range(1, 15, 3):
#     print(i)

# for i in range(len(animals) - 1, 3, -1):
#     print(animals[i])


# for i in range(5):
#     input(f"Enter num {i + 1}: ")


# Quickly write a program that asks a user to provide a number, and then do a count down from that number to 3

# user_num = int(input('Enter countdown start: '))
# for i in range(user_num, 2, -1):
#     print(i)





animals = ["Hippo", "Elephant", "Cheetah", "Falcon", "Eagle", "Leopard", "Jaguar"]
# for i in range(len(animals)):
#     print(animals[i][-1])

# For-each loop

# for animal in animals:
#     print(animal)


# For each letter in the string "animal", print each letter 3 times.

# for ch in "animal":
#     print(ch * 3)


# books = [
#     {"author": "Tobi Dada", "title": "Coding for Beginners"},
#     {"author": "Kevin Mitnick", "title": "Ethical Hacking Introduction"}
# ]

# for book in books:
#     print(book['title'])


# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}

# for capital in capitals.items():
#     print(capital)


# for country, capital in capitals.items():
#     # print(capital)
#     print(f"Country: {country} ---->>> {capital}")

# Country:     ----> 

# my_string = "Python is fun!"
# for char in my_string:
#     print(f"Character: {char}")



# tasks = ["start", "process", "skip", "finish"]
# for x in tasks:
#   if x == "skip":
#     continue
#   print(x)



# Let's have a list of games

# games = ["C.O.D", "Devil May Cry", "Prince of Persia", "Fifa 50", "Batman", "Mortal Kombat", "Spiderman"]

# # for game in games:
# #     print(game)

# # for i in range(len(games)):
# #     print(f"{i+1}. {games[i]}")

# for index, game in enumerate(games, start=1):
#     print(f"{index}. {game}")


# employees = ["John Doe", "Mark Nsukkabread", "Martin Martina", "Luke Cage"]

# print("EMPLOYEE\t\t\tEMPLOYEEID")

# for id, emp in enumerate(employees, start=101):
#     print(f"{emp}\t\t\t{id}")

# # EMPLOYEE                  EMPLOYEEID
# JOhn Doe                    101
# Mark Nsukkabread            102