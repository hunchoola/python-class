"""
Create a dictionary called `student` with keys "name", "age", and "grade", and 
corresponding values "John", 20, and "A". Access and print the value of "name".
"""

student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

print(student["name"])

"""
Create a dictionary called `product` with keys "name", "price", and "stock", and 
corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
"""

product = {
    "name": "Laptop",
    "price": 999.99,
    "stock": 50
}

product["price"] = 899.99

print(product)

"""
Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000."""

employee = {
    "name": "Alice",
    "position": "Manager",
}

employee["salary"] = 50000

print(employee)

"""
Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana"."""

inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

del inventory["banana"]
print(inventory)


"""
Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy."""

person = {
    "name": "Bob",
    "age": 25,
    "city": "New York"
}

person_copy = person.copy()

print(person_copy)


"""
Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2"."""

family = {
    "child1": {
        "name": "Bolade",
        "age": 23
    },

    "child2": {
        "name": "Adebayo",
        "age": 21
    },

    "child3": {
        "name": "Jessica",
        "age": 19
    }
}

print(family["child2"]["age"])

"""
Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model"."""

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}

print(car["model"])

"""
Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish"."""

settings = {
    "volume": 50,
    "brightness": 75,
    "language": "English"
}

settings["language"] = "Spanish"

print(settings)

"""
Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science"."""

score = {
    "math": 90,
    "science": 85,
    "english": 88
}

del (score["science"])
print(score)

"""
Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary."""

menu = {
    "starter": "Soup",
    "main_course": "Steak",
    "dessert": "Ice Cream"
}

check_value = "appetizer" in menu

print(check_value)
