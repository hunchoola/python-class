"""
Write a function sum_numbers(a, b) that returns the sum of two numbers."""

# def sum_number(num1, num2):
#     sum_num = num1 + num2
#     print(sum_num)

# sum_number(34, 50)

"""Write a function is_even(n) that returns True if n is even and False if n is odd.
"""

# def is_even(n):
#     if n % 2 == 0:
#         print(True)
#     else:
#         print(False)

# is_even(45)

"""Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
"""

# def is_prime(n):
#     if n % 1 == 0 and n % n

"""4 Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
"""

"""5 Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
"""

# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)

#     else:
#         return max(a, b)

# print(lesser_of_two_evens(5, 20))

"""
Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
is_alliteration(‘Levelheaded llama’) —> True
is_alliteration(‘Crazy Kangaroo’) –> False"""

# def is_alliteration(two_word_string):
#     split_list = two_word_string.lower().split(" ")
#     return split_list[0][0] == split_list[1][0]

# print(is_alliteration("Akeem AkanniOla"))

"""Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
old_macdonald(‘macdonald’) —> MacDonald
Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald."""

# def old_macdonald(name):
#     splitname = name[:3].title() + name[3:].title()
#     return splitname

# print(old_macdonald("macdonald"))

"""8 Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
spy_game([1, 7, 2, 0, 4, 5, 0]) —> False"""

# def spy_game([list_of_ints]):

"""Write a function vol(radius) that computes the volume of a sphere given its radius."""

# def vol(radius):
#     return (4/3) * 3.14 * (radius ** 3)

# print(vol(2))


"""10 Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low)."""


"""Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters."""

# def upper_lower(text):
#     uppercase = 0
#     lowercase = 0
#     for char in text.replace(" ", ""):
#         if char.isupper():
#             uppercase += 1
#         else:
#             lowercase += 1
#     print(f" Uppercase : {uppercase}")
#     print(f" lowercase : {lowercase}")

# upper_lower("Hello Beautiful Love")


"""Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor."""

# def unique_list(list_items):
#     unique = []
#     for item in list_items:
#         if item not in unique:
#             unique.append(item)

#     return unique

# print(unique_list([2, 4, 5, 5, 2, 1]))

"""Write a function multiply(list_items) to multiply all the numbers in a list.
	Sample List: [1, 2, 3, -4]
	Expected output: -24"""

# def multiply(list_items):
#     total = 1
#     for num in list_items:
#         total *= num
#     print(total)

# list = [2, 4, 5, 5, 2, 1]
# multiply(list)

""" 14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
	least once. For example: “The quick brown fox jumps over the lazy dog”.
	Hint: Import and use the string module."""

# import string


# def is_pangram(text):
#     string.ascii_lowercase
#     text_lower = text.lower()
#     for chat in text:
#         for char in string.ascii_lowercase:
#             return True
#         else:
#             return False

# print(is_pangram("hello world"))

"""Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
	(BMI) given weight in kilograms and height in meters."""


# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     print(bmi)


# calculate_bmi(70, 1.7)


"""Write a function calculate_simple_interest(principal, rate, time) that calculates the 
	simple interest given principal amount, interest rate, and time (in years)."""


# def calculate_simple_interest(principal, rate, time):
#     simple_interest = principal * rate * time / 100
#     print(simple_interest)

# calculate_simple_interest(20000, 10, 2)