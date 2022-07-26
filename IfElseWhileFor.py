"""1. Print First 10 natural numbers using while loop."""

# i = 0
# while i < 10:
#     print(i,end=" ")
#     i+=1


"""Calculate the sum of all numbers from 1 to a given number"""

# n = int(input("Enter a limit:"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print("Sum of numbers:",sum)


"""Write a program to print multiplication table of a given number"""

# n = int(input("Enter a number:"))
# for i in range(1,11):
#     print(i*n)


"""Display numbers from a list using loop"""

# li = [10, 20, 90, 80, 70, 40]
# for i in li:
#     print(i)

"""Count the total number of digits in a number"""

# n = int(input("Enter a number greater than 10: "))
# sum = 0
# while n > 0:
#     d = n % 10
#     sum = sum + d
#     n = n//10
# print("Sum of the digits:",sum)


"""Print the following pattern"""
"""1. Print list in reverse order using a loop"""
# li = ["a", "b", "c", "d", "e"]
# for i in range(len(li)-1,-1,-1):
#     print(li[i])


"""2. Display numbers from -10 to -1 using for loop"""
# for i in range(-10,0,1):
#     print(i)

"""Use else block to display a message “Done” after successful execution of for loop"""
# for i in range(1,11):
#     print(i)
# else:
#     print("Done")

"""Write a program to display all prime numbers within a range"""

# n1 = int(input("Enter a lower limit:"))
# n2 = int(input("Enter a upper limit:"))
# for i in range(n1,n2+1):
#     if i > 0:
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)

"""Display Fibonacci series up to 10 terms"""
# n1=0
# n2=1
# for i in range(1,11):
#     print(n1)
#     sum = n1 + n2
#     n1 = n2
#     n2 = sum


"""Find the factorial of a given number"""
# n = int(input("Enter a number:"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)


"""Reverse a given integer number"""
# n = int(input("Enter a number greater than 10: "))
# while n > 0:
#     d = n % 10
#     print(d,end="")
#     n = n//10


"""Use a loop to display elements from a given list present at odd index positions"""
# li = ["a", "b", "c", "d", "e", "f"]
# for i in range(1,len(li),2):
#     print(li[i])


"""Calculate the cube of all numbers from 1 to a given number"""
# n = int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(i*i*i)


"""Find the sum of the series upto n terms"""
sum = 0
n = int(input("Enter a number:"))
for i in range(1,n+1):
    sum = sum + i
print(sum)
