"""Write a program that takes an integer input from the user and uses a loop to calculate 
the sum of its digits. Print the sum. Example:
Input: 1234
Output: 10 (1+2+3+4)
"""

# user_num = input("Enter Number/s : ")
# total = 0
# for digit in user_num:
#     print(digit, end=" ")
#     total = total + int(digit)
# print()
# print(f"The Sum is {total}")


"""Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
Input: "hello world"
Output: Vowels: 3, Consonants: 7
"""

# user_input = input("Enter a String : ")
# vowel = 0
# consonants = 0

# user_input = user_input.lower()

# for char in user_input:
#     if char in "aeiou":
#         vowel = vowel + 1
#     elif char.isalpha():
#         consonants = consonants + 1
# print(vowel)
# print(consonants)


"""
Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
Input: 5
Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
"""

# table = 5

# for i in range (1, 13):
#     print(f"{table} * {i} = {table * i}")

"""
Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
Example:
Input: "python"
Output: "nohtyp"
"""
# user_input = input("Enter a String : ")
# reversed_string=""
# for i in range(len(user_input -1, -1, -1)):
#     print(user_input{i})


# """Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]"""

# user_num = input("Enter numbers seperated with commas : ").split()

# new_num = []
# for num in user_num:
#     if num in new_num:
#         new_num.append(num)
#     print(new_num)

"""
	Write a program that takes an integer n from the user and calculates the sum of all 
	even numbers from 1 to n. Print the sum.
	Input: 10
	Output: 30 (2 + 4 + 6 + 8 + 10)"""

# user_num = int(input("Enter a number : "))
# total = 0

# for num in range(1, user_num):
#     if num % 2 == 0:
#         total = total + num
# print(total)

# countries = ["nigeria", "belgium", "benin", "laos", "ghana", "ethiopia"]
# vowel = "aeiou"
# for country in countries:
#     if country[1] not in vowel:
#         print("There is a country with second letter is vowel")
#         break

# countries_with_vowels_last = []
# countries = ["nigeria", "belgium", "benin", "laos", "ghana", "ethiopia"]
# vowel = "aeiou"
# for country in countries:
#     if country[-1] in vowel:
#         countries_with_vowels_last.append(country)
# print(countries_with_vowels_last)
    
# multiple_5 =[]
# numbers = [2, 5, 2, 5, 28, 68, 28, 19, 25, 35, 29, 40, 82]
# for num in numbers:
#     if num % 5 == 0:
#         multiple_5.append(num)
# print(multiple_5)


name = "Tobi"
list_of_letter = []

for ch in name:
    list_of_letter.append(ch.isupper())
    
if any (list_of_letter):
    print('There is atleast one upper')
    
else:
    print("no")