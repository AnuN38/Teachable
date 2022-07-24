"""Print the sum of the current number and the previous number"""

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)


"""Print characters from a string that are present at an even index number"""

# st = input("Enter a string: ")
# i = 0
# while i < len(st):
#     print(st[i])
#     i = i + 2


"""Remove first n characters from a string"""

st = input("Enter a string: ")
n = int(input("Enter a number: "))
if len(st) >= n:
    for i in range(0,len(st)):
        if i > n:
            print(st[i], end="")