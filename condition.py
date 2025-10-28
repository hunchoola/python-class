# word = input('Enter a word: ').lower()
# last_4 = word[-4:]
# reverse_word = last_4[::-1]
# if reverse_word == last_4:
#     print(f"The last four {last_4} is Palidromic")
# else:
#     print(f"The last four {last_4} is not Palidromic")

colors = set(input("Enter Three colors seperated with comma: ").split(', '))
primary_color = {"red", "blue", "yellow"}

if colors == primary_color:
        print("All primary colors")
else:
        print("Not all primary colors")



