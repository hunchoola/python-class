"""Print numbers from 1 to 5
Expected Output:
1
2
3
4
5
"""

i = 1
while i <= 5:
    print(i)
    i += 1

"""
Print "Hello" 3 times
Expected Output:
Hello
Hello
Hello
"""

i = 1
while i <= 3:
    print("Hello")
    i += 1

"""Print only even numbers from 2 to 10 (do not use += 2)
Expected Output:
2
4
6
8
10
"""

i = 2
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

"""
Print numbers in reverse from 5 to 1 using a while loop.
Expected Output:
5
4
3
2
1
"""

i = 5
while i >= 1:
    print(i)
    i -= 1

"""
Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
Expected Output:
1
2
3
4
6
7
8
9
10
"""

i = 1
while i <= 10:
    if i != 5:
        print(i)
    i += 1

    """
    Print a square of stars
Ask the user to enter a number
Example 1:
Input: 3

Output:
***
***
"""
repeat_time = int(input("Enter the Number of times : "))
i = 1
while i <= repeat_time:
    print("***")
    i += 1

"""
Print a right triangle of stars
Ask the user to enter a number
Example:
Input: 4

Output:
*
**
***
****
"""

repeat_time2 = int(input("Enter the Number of times : "))
i = 1
while i <= repeat_time2:
    print("*" * i)
    i += 1

"""
Print a countdown
Ask the user to enter a number where they want to start the countdown from.
Example:
Input: 5

Output:
5
4
3
2
1
Go!
"""
Start_count=int(input("Enter a number : "))
i = Start_count
while i >= 1:
    print(i)
    i -= 1
print("Go!")


"""
Print "1" ten times on the same line using a while loop
Expected Output:
1111111111
"""

# print("1" * 10)