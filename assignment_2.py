# Create a variable named `car_name` and assign the value Volvo to it.
car_name = "volvo"
print(car_name)

# Create a variable named x and assign the value 50 to it.
x = 50
print(x)

# Which of the following variable names is legal in Python?
_variable3 = "is corect"

# Which of the following assignment statements is safe in Python?
None

# Declare variables name, age, height, and is_student, and assign them values of different types. Print the type of each variable.

name = "Olamide"
age = 10
height = 5.1
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.

first_name = "John"
last_name = "Doe"
print(first_name + " " + last_name)


# Create a string variable message with the value "Hello, ". Interpolate the variable name (assigned the value "Alice") into the message and print the result.


name = "Alice"
print(f"Hello, {name}")


# Create a multi-line string variable using triple quotes.
full_name = "Arikeuyo Akeem Olamide"
gender = "male"
school = "Leadcity university"
level = "Msc"
occupation = "Farmer"

Details = f"""Personal Information
Name: {full_name}
Sex: {gender}
Institution: {school}
Education Level: {level}
Occupation: {occupation}"""

print(Details)

# Create a string variable word with the value "Python". Print the first and last characters using indexing.
a = "Python"
print(a[0], a[5])

# Attempt to modify the character at index 2 in the string "Python" from question 9. Print the resulting error message.

# a[2] = "S"

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)


# Assign the values 10, "John", and True to the variables age, name, and is_student in a single line.

age, name, is_student = 10, "John", "True"
print(age)
print(name)
print(is_student)


# Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.

x = 5
y = 10

x, y = y, x

print(x)
print(y)

# Create a list of numbers with values 1, 2, and 3. Unpack the list into separate variables a, b, and c.

number = [1, 2, 3]
a, b, c = number
print(a)
print(b)
print(c)

# Convert a string variable called height from “1.35” to a float.

height = "1.35"
convert_ht = float(height)
print(convert_ht)
print(type(convert_ht))
