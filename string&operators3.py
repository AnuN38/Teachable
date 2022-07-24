"""
1)Write a program to create a new string made of the middle three characters of an input string.

2)Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

3)Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

4)Count all letters, digits, and special symbols from a given string

5)Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
"""

mid = input("Enter three characters: ")
a = "python strings {} characters"
print(a.format(mid))

s1 = "Hello {} world"
s2 = "Anu nallatt"
s3 = s1.format(s2)
print(s3)

x = "AnuNALLatt"
l = ""
u = ""
for i in x:
    if i.islower():
        l = l + i
    else:
        u = u + i
print(l + u)

s = "Python123*PROGRamming #language."
l2 = 0
d = 0
sc = 0
for i in s:
    if i.isalpha():
        l2 = l2 + 1
    elif i.isdigit():
        d = d + 1
    else:
        sc = sc + 1
print("Letter count:", l2)
print("Digit count:", d)
print("Special symbol count:", sc)

S1 = "HelloWorldHai"
S2 = "AnuNallatt"
l1 = len(S1)
l2 = len(S2)
if l1 > l2:
    length = l1
else:
    length = l2
S2 = S2[::-1]
result = ""
for i in range(length):
    if i < l1:
        result = result + S1[i]
    if i < l2:
        result = result + S2[i]
print(result)
