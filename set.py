# Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in
# the set and print the result.

fruits = {"air", "water", "food"}
a = "food" in fruits
print(a)


# Create a set called colors with values {"red", "green", "blue"}. Add the color "yellow"
# to the set and print the updated set.
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)

# Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to the set and print the updated set.

animals = {"cat", "dog", "rabbit"}
animals.update(["horse", "sheep"])
print(animals)


# Create a set called countries with values {"USA", "Canada", "Mexico"}. Remove "Canada" from the set and print the updated set.

countries = {"USA", "Canada", "Mexico"}
countries.remove("Canada")
print(countries)

# Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in the set without raising an error.


cities = {"New york",  "Los Angeles", "Chicago"}
cities.discard("Hoston")
print(cities)

# Given the list seasons = ["Spring", "Summer", "Fall", "Winter", “Spring”], convert the list to a set to get rid of the duplicate `Spring`.

season = ["spring", "Summer", "Fail", "Winter", "Spring"]
season = set(season)
print(season)

"""Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets and print the result.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

all_set = set1.union(set2)
print(all_set)

"""Given two sets, setA = {"a", "b", "c"} and setB = {"c", "d", "e"}, find the intersection of the sets and print the result."""

setA = {"a", "b", "c"}
setB = {"c", "d", "e"}

set_intersect = setA.intersection(setB)
print(set_intersect)

"""
Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print the updated set."""

prime_numbers = {2, 3, 5, 7}
prime_numbers.add(11)
print(prime_numbers)

"""
Given the set odd_numbers = {1, 3, 5, 7, 9}, remove a random item from the set and print the updated set."""

odd_numbers = {1, 3, 5, 7, 9}
removed = odd_numbers.pop()
print(odd_numbers)

"""
Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result."""

vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)

"""
Given the set letters = {"a", "b", "c"}, find the difference between `letters` and another set {"b", "c", "d"}. Print the result. Afterwards, find the symmetric difference and print the result."""

letters = {"a", "b", "c"}
other_letters = {"b", "c", "d"}

difference_letters = letters.difference(other_letters)
print(difference_letters)

symmetric_difference = letters.symmetric_difference(other_letters)

print(symmetric_difference)

"""
Create a set called tech_brands with values {"Apple", "Google", "Microsoft"}. Add the items from another set {"Amazon", "Facebook"} and print the updated set tech_brands without creating a new set."""

tech_brands = {"Apple", "Google", "Microsoft"}
other_brands = {"Amazon", "Facebook"}

tech_brands.update(other_brands)
print(tech_brands)

"""
	Create a set called students with values {"Alice", "Bob", "Charlie", "David"}. Use the 
	remove method to remove "Charlie" from the set and print the updated set. Then try to 
	remove "Eve" from the set and observe the behavior."""

students = {"Alice", "Bob", "Charlie", "David"}
students.remove("Charlie")
print(students)

# students.remove('Eve')
# print(students)


"""
Given a list numbers_list = [1, 2, 3, 4, 4, 5, 5], convert this list to a set to remove 
	duplicates and print the resulting set."""

numbers_list = [1, 2, 3, 4, 4, 5, 5]
numbers_list = set(numbers_list)
print(numbers_list)

"""
	Given a string text = "hello", convert this string to a set to find the unique 
	characters and print the resulting set."""

text = "hello"
unique_chars = set(text)
print(unique_chars)

"""
Create a set called vehicles with values {"car", "bike", "bus", "train"}. Find out how 
	many items are in the set and print the result."""

vehicles = {"car", "bike", "bus", "train"}
num_items = len(vehicles)
print(num_items)


"""
Given the set gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}, print the 
	number of items in the set."""

gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}
gadgets_num = len(gadgets)
print(gadgets_num)
