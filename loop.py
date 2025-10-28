# i = 1
# while i <= 4:
#     input("Enter your name 4x : ")
#     i += 1


# i = 1
# while i <=12:
#     print(f"15 * {i} = {i*15}")
#     i+=1


# i = 1
# while i <= 200:
#     if i % 3 ==0:
#         print(i)
#     i +=1

# i =1
# total = 0
# while i <= 5:
#     num = int(input("Enter a number"))
#     total += num
#     i += 1
# print(total)

# time_to_repeat = int(input("Enter the number of times you want to multiply : "))
# i = 1
# while i <= time_to_repeat:
#     print(f"15 * {i} = {i*15}")
#     i+=1

total_odd = 0
i = 1
while i <= 490:
    if i % 2 == 1:
        total_odd += i
    i +=1

print(total_odd)
