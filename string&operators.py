"""
a)Define the string "FUTURA" into a variable and string "LAB" into another variable
b)print the first and last character of the first string
c)concatenate two strings into new string
d)find length of new string
e)print UTURA LA of the string
f)print first 3 characters of the string
g)print the reversal of the string
[ using slicing]
h)Delete the first string   """


x = "FUTURA"
y = "LAB"

print("First character: ",x[0])
print("Last character: ",x[len(x)-1])

z = x + y
print(z)

print("Length of ",z,"is",len(z))

z = x[1:6]
w = y[0:2]
print(z,w)

print("First 3 characters of the string",x[:3])
print("First 3 characters of the string",y[:3])

print("Reverse of the string:",x[::-1])
print("Reverse of the string:",y[::-1])

del x
print(x)