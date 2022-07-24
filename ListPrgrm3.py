"""1. Python program to interchange first and last elements in a list."""

# li = ["a","b","c","d","e"]
# l = len(li)
# temp = li[0]
# li[0] = li[l-1]
# li[l-1] = temp
# print(li)

"""2. Python program to find smallest number in a list."""
# li2 = [4, 9, 12, 5, 2, 15, 5]
# li2.sort()
# print("Smallest number is :",li2[0])

"""OR"""

# li2 = [4, 9, 12, 5, 2, 15, 5]
# smallest = li2[0] if li2 else None
# for i in li2:
#     if i < smallest:
#         smallest = i
# print("Smallest element is: ", smallest)


"""3. Write a python program to print even numbers in a list."""
# li3 = [4, 5, 3, 8, 6, 13, 15]
# even = []
# for i in li3:
#     if i%2 == 0:
#         even.append(i)
# print(even)


"""4. Write a python program to print odd numbers in a list."""
# li4 = [4, 5, 3, 8, 6, 13, 15]
# odd = []
# for i in li4:
#     if i%2 != 0:
#         odd.append(i)
# print(odd)

"""5. Write a python program to print positive numbers in a list."""
# li5 = [2,8,-5,-4,6,-1]
# for i in li5:
#     if i > 0:
#         print(i)


"""6. Write a python program to print negative numbers in a list."""
# li5 = [2,8,-5,-4,6,-1,0]
# for i in li5:
#     if i < 0:
#         print(i)

"""7. Write a python program to covert Fahrenheit to Celsius."""
# f = float(input("Enter fahrenheit value:"))
# c = ((f-32)*5)/9
# print("Celsius value is:",c)

"""8. Write a python program to print maximum and minimum number in a tuple."""
# t8 = (4, 20, 9, 10, 5, 12, 6)
# print("Minimum:",min(t8))
# print("Maximum:",max(t8))

"""9. Write a python program to convert a list into a tuple."""
# li9 = ["a","b","c","d","e"]
# tp = tuple(li9)
# print(tp)
# print(type(tp))

"""10. Write a python program to create a list and use the following functions-
•append() and extend()
•len()
•membership (in, not in)"""

x = ['a', "b", "c", "d", "e"]
x.append("f")
print(x)

a = ["anu", "sam", "ram", "rinu"]
b = [1, 2, 3, 4, 5, 6]
a.extend(b)
print(a)

print(len(a))
print(len(b))

w = ["apple","orange","grape","kiwi"]
if "apple" in w:
    print("Yes present")
else:
    print("Not present")

h = ["a","b","c","d"]
if "c" not in h:
    print("Wrong")
else:
    print("Correct")



