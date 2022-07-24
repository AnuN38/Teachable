"""
a). Define a string "Python is a programming language that lets you work quickly and integrate systems more effectively".
b). change into lower case and uppercase.
c) replace every ‘a’ with "*"
d). check if there is 'you' in the string, then print “FOUND”
"""


a = "Python is a programming language that lets you work quickly and integrate systems more effectively"
print(a)

print(a.lower())
print(a.upper())

print(a.replace("a","*"))


if "you" in a:
    print("FOUND")
