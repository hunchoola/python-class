
# print("Available categories: Motivation, Love, Wisdom")

# user_choice = input("Enter a category: ").lower()
    

# if user_choice == "motivation":
#         print('Quote: "Beliving in yourself is the first and most crucial part of achieving your goal."')
    
# elif user_choice == "love":
#         print('Quote: "Love is not what you say, love is what you do."')
    
# elif user_choice == "wisdom":
#         print('Quote: "The only true wisdom is in knowing you know nothing."')
    
# else:
#         print("Category not found. Please choose from: Motivation, Love, Wisdom")


#         import random

from random import randint

user_name = input('Enter your user name : ')
email = input('Enter your email : ')
password = input('ENter Your password : ')

generate_otp = randint(1000, 9999)

print(f' {user_name} Your otp is {generate_otp}')

user_otp = int(input('input the otp sent to you  : '))

if generate_otp == user_otp:
    print('You have been verified')
else:
    print('Your Otp is not correct Please enter correct otp')