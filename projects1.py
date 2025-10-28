# # A customer has 10000 in their account. Let them withdraw an amount and if it is greater than balance, print insufficient funds, if it is equal to balance, print accoutn will be empty. Otherwise, print successful and the new balance.

# user_balance = 10000

# withdrawal_amount = float(input("Enter withdrawal amount: "))

# if user_balance < withdrawal_amount:
#     print(f"Insufficient funds. Your current balance is: {user_balance}")
# elif user_balance == withdrawal_amount:
#     print("Your account will be empty.")
# else:
#     # new_blance = user_balance - withdrawal_amount
#     # user_balance = user_balance - withdrawal_amount
#     user_balance -= withdrawal_amount
#     print(f"Withdrawal successful!\nYour new balance is: {user_balance}")




# The price of an item is 5000. Ask the user for a coupon code and if they enter SAVE10, give 10% discount... SAVE20... 20%. Otherwise, return the full price.

# price = 5000
# coupon_code_list = ['SAVE10', 'SAVE20']
# coupon_code = input("Enter coupon code: ")

# if coupon_code not in coupon_code_list:
#     print("Invalid coupon code.")
#     exit()


# if coupon_code == coupon_code_list[0]:
#     new_price = price * 0.9
#     print(f"10% Discount applied. Total price now: {new_price}")
    
# elif coupon_code == coupon_code_list[1]:
#     new_price = price * 0.8
#     print(f"20% Discount applied. Total price now: {new_price}")
# else:
#     print(f"0% Discount applied. Total price {price}")





# haev a variable caled user and store the user login details in it. Then ask a user to provide their own login credentials. And if they match what is in the user details you stored, say login successful.

# user = {"username": "user11", "password": "pass@word"}

# username = input('Enter your username: ') 
# password = input('Enter your password: ')
# if username != user['username']:
#     print("This username does not exist")
# elif username == user['username'] and password == user['password']:
#     print("Login successful")
# else:
#     print("Password is incorrect")
    




#****************************** Student payment status Program ***********************
# student_payment_status = {
#     "Ada": True,
#     "Bolu" : False,
#     "Chioma": True,
#     "Tobi": True,
#     "Tade": True,
#     "David": False
# }

# student_name = input('Enter student name: ') # Tobi

# if student_name not in student_payment_status:
#     print(f"{student_name} does not exist among your students")
#     exit()


# if student_payment_status[student_name]:
#     print('Fee paid')
# else:
#     print("Fee not paid.")






# ask the user how much airtime they want to reccharge. If the amount is 1000 or more... Give 20% bonus. If it is 500 or more, give 10%. Otherwise, no bonus. Then print the total bonus and the total airtime received.

# ********************** FIRST METHOD **********************

# recharge_amount = float(input("Enter recharge amount: "))

# if recharge_amount >= 1000:
#     bonus = 0.2 * recharge_amount
#     recharge_amount += bonus
#     print(f"You got {bonus} bonus. Your total airtime is: {recharge_amount}")
# elif recharge_amount >= 500:
#     bonus = 0.1 * recharge_amount
#     recharge_amount += bonus
#     print(f"You got {bonus} bonus. Your total airtime is: {recharge_amount}")
# else:
#     print("You do not qualify for a bonus. Your total airtime is:", recharge_amount)



# ********************** SECOND METHOD **********************


# recharge_amount = float(input("Enter recharge amount: ")) # 8000
# bonus = 0
# if recharge_amount >= 1000:
#     bonus = 0.2 * recharge_amount
# elif recharge_amount >= 500:
#     bonus = 0.1 * recharge_amount

# recharge_amount += bonus
# print(f"You got {bonus} bonus. Your total airtime is: {recharge_amount}")








# *******************************   Simple guess game  ***************************

# Let the computer generate the number
# import random

# score = 0
# computer_guess = random.randint(1, 50)
# print(f"Hint: {computer_guess}")

# user_guess = int(input('Guess the number (between 1 - 5): '))

# if computer_guess == user_guess:
#     score += 50
#     print("Wow!!! Correct guess!!")
# else:
#     print("Sorry, man! Try again!!!")


# print(f"Your total score is: {score}")