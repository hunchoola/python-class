"""Handle Multiple Exceptions:
Write a function safe_divide(a, b) that performs division.
Handle ZeroDivisionError if the divisor is zero.
Handle TypeError if the inputs are not numbers.
Handle ValueError if the inputs are not convertible to floats.
"""


# def safe_divide(a, b):
#     try:
#         a = float(a)
#         b = float(b)

#         divsion = a / b

#     except ZeroDivisionError:
#         print("You cannot devide by zero")
#     except TypeError:
#         print("Operation can only be perform on Numbers")
#     except ValueError:
#         print("Please make sure your input are interger (numbers)")
#     except Exception:
#         print("An Error Just Happened")
#     else:
#         print(divsion)

# safe_divide(10, 2)

# start_with_vowel = 0
# atleast_5_letter = 0
# file = open("words.txt")
# content = file.read().split()
# for words in content:
#     if words[0] in "aeiou":
#         start_with_vowel += 1
#     if len(words) >= 5:
#         atleast_5_letter += 1

# print(start_with_vowel)
# print(atleast_5_letter)


# with open("number_with_exponents.txt", "w") as file:
#     for i in range(1, 101):
#         file.write(f"{i}, {i**2}, {i**3}\n") 


import requests


user_word = input("Enter a Word: ")



with open("extract.txt", "w") as file:
    url = 'https://newyork.craigslist.org/search/sss#search=2~gallery~0'
    response = requests.get(url)
    html_content = response.text
    file.write(html_content)
