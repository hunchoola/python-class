# capitalize
goal = "the goal is to empower local development teams"
cap = goal.capitalize()
print(cap)


# title
goal = "the goal is to empower local development teams"
title = goal.title()
print(title)


# count
goal = "the goal is to empower local development teams"
count = goal.count("o")
print(count)


# startwith
goal = "the goal is to empower local development teams"
startswith = goal.startswith("go")
print(startswith)


# endswith
goal = "the goal is to empower local development teams"
endswith = goal.endswith("teams")
print(endswith)


# find
goal = "the goal is to empower local development teams"
findgoal = goal.find("o")
print(findgoal)

# format
goal = "I am {name} and i am {gender}".format(name="Akeem", gender="male")
print(goal)

# islower
lowergoal = "Olamide".islower()
print(lowergoal)

# isupper
goalupper = "Olamide".isupper()
print(goalupper)

# lstrip
akgoal = " Atirola".lstrip()
print(akgoal)

# lower
textlower = "HELLO".lower()
print(textlower)

# upper
textupper = "hello".upper()
print(textupper)

# strip

textstrip = " Hello There ".strip()
print(textstrip)

# replace
print("Hello world".replace("world", "There"))

# split
txt = "By@developing@a@localized@Agile@framework"
x = txt.split("@", 5)
print(x)

# join
course = ["softwareEngr", "computerScience", "English"]
x = ("#").join(course)
print(x)
