"""Python Functions"""

"""Find the reverse of a number"""
# def reverse(n):
#     while n > 0:
#         d = n % 10
#         print(d,end="")
#         n = n // 10
# num = int(input("Enter a number greater than 10: "))
# reverse(num)

"""Create a recursive function to find the sum of numbers"""


# def findSum(n):
#     if n <= 1:
#         return n
#     else:
#         return n + findSum(n - 1)
#
# num = int(input("Enter a number:"))
# s = findSum(num)
# print(s)


"""Define a function that accepts 2 values and return its sum, subtraction and multiplication"""
# def operation():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number:"))
#     sum = a + b
#     subtraction = a - b
#     mul = a * b
#     return sum,subtraction,mul
#
# op = operation()
# print(op)


"""Define a function which counts vowels and consonants in a word"""
# def countVC(s):
#     s.lower()
#     vCount = 0
#     cCount = 0
#     for i in s:
#         if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             vCount+=1
#         else:
#             cCount+=1
#     print("Vowels count:",vCount)
#     print("Consonants count:",cCount)
# st = input("Enter a word:")
# countVC(st)


"""Define a function that accepts radius and returns the area of a circle"""
def AreaCircle():
    r = float(input("Enter the radius of the circle:"))
    a = 3.14 * r * r
    return a
ar = AreaCircle()
print("Area of circle:",ar)