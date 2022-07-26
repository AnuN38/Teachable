"""1. Write a statement to write the string”Welcome! Please have a seat” in the file wel.txt,
that has not yet been created."""

# f = open("wel.txt","x")
# f.close()
# f = open("wel.txt","w")
# f.write("Welcome! Please have a seat")
# f.close()


"""2.Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”."""
# f = open("PYTHON.TXT","x")
# f.close()

# file = open("PYTHON.TXT","w")
# file.write("Python was designed for readability, the has some similarities to the English language with influence from mathematics.Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.")
# file.close()

# count = 0
# file = open("PYTHON.TXT","r")
# data = file.read()
# for i in data:
#     if i.isupper():
#         count = count + 1
# print(count)
# file.close()

"""3.Write a program to display all the lines in a file “python.txt” along with line/record number."""
file = open("PYTHON.TXT","r")
count=0
rec=""
while True:
    rec=file.readline()
    if rec=="":
        break
    count=count+1
    print(count,rec)
file.close()


