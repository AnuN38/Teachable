"""1)Write a Python program to sum all the items in a list."""

sum = 0
li = [6, 12, 15, 5, 9, 15, 20, 2]
for i in li:
    sum = sum + i
print(sum)


"""2)Write a Python program to multiply all the items in a list."""

mul = 1
li2 = [6, 12, 15, 5, 9, 15, 20, 2]
for i in li2:
    mul = mul * i
print(mul)


"""3)Write a Python program to convert a tuple to a string."""

t1 = ("apple","orange","pineapple","grape")
for i in t1:
    print(i)


"""4)Write a Python program to convert a list to a tuple"""

li3 = ["apple","orange","pineapple","grape"]
t2 = tuple(li3)
print(t2)
print(type(t2))
