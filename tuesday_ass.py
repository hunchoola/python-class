""". Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# after, print the result of the function.
# For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]
"""
# names = ["Winifred", "Wilfred", "Justin", "Augusta"]

# def turn_to_upper(names):
#     name_upper = []
#     for name in names:
#         name_upper.append(name.upper())
#     return name_upper

# test = turn_to_upper(names)
# print(test)

"""
Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys "first", "middle", and "last".
# The function should return only the middle name.
# For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"}, then the result would be "James". Another example is if name_dict is {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".
"""
# name_dict = {"first": "Tola", "middle": "James", "last": "Akin"}

# def get_middle_name(name_dict):
#     return name_dict.get["middle", "N/A"]

# test = get_middle_name(name_dict)
# print(test)

"""
# 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# For example, if the string is "Python", the result would be "nohtyP".
"""
# user_input = input("Enter a string : ")
# def reverse_string(user_input):
#     return user_input[::-1]

# test = reverse_string(user_input)
# print(test)

"""4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# For example, if the string is "beautiful", the result would be 5.
"""

# def count_vowels(user_input):
#     count = 0
#     vowel = ("a, e, i, o, u")
#     for char in user_input:
#         if char in vowel:
#             count += 1
#     return count

# user_input = input("Enter a string : ")
# num_of_vowels = count_vowels(user_input)
# print(f' {user_input} has {num_of_vowels} vowels')

"""
# 5. Create a function called even_numbers that takes in a list of integers and returns a new list containing only the even numbers.
# For example, if the list is [1, 2, 3, 4, 5, 6], the result would be [2, 4, 6].
"""
# numbers = [1, 2, 3, 4, 5, 6]


# def even_numbers(numbers):
#     evens = []
#     for num in numbers:
#         if num % 2 == 0:
#             evens.append(num)
#     return evens


# test = even_numbers(numbers)
# print(test)


"""
 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# For example, if the list is [12, 45, 3, 67, 23], the result would be 67.
"""

# numbers = [12, 45, 3, 67, 23]


# def find_max(num):
#     return max(numbers)


# test = find_max(numbers)
# print(test)


"""Create a function called sum_dict_values that takes in a dictionary with numeric values and returns the sum of all the values.
# For example, if the dictionary is {"a": 10, "b": 20, "c": 5}, the result would be 35.
"""
# dict = {"a": 10, "b": 20, "c": 5}
# def sum_dict_values(dict):
#     dict_sum = sum(dict.values())
#     return dict_sum

# test = sum_dict_values(dict)
# print(test)

"""8. Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# For example, if the list is ["apple", "banana", "cherry"], the result would be {"apple": 5, "banana": 6, "cherry": 6}.
"""


# list_words = ["apple", "banana", "cherry"]
# def word_lengths(words):
#     for word in list_words:

#         return {word: len(word)}
    
# test = word_lengths(list_words)
# print(test)



"""
Create a function called is_palindrome that takes in a string and returns True if the string is a palindrome (same forwards and backwards), otherwise False.
# For example, if the string is "level", the result would be True. If the string is "hello", the result would be False.
"""

# def is_palindrome(text):
#     print(text == text[::-1])



# is_palindrome("refer")

    
