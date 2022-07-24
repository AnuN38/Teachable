"""
1.create a list with name of fruits with size of 4

2.Create another list with name of vegetables with size of 3

3.Insert "cat" in the fruit list to the index 2

4.append the fruit to vegetable list

5.sort the list

•fruit list---->ascending order

•vegetable list------> descending order

6.Make a copy of fruit list

7.reverse the vegetable list
"""

"""1.create a list with name of fruits with size of 4"""
fruits = ["apple","orange","banana","grape"]
print(fruits)

"""2.Create another list with name of vegetables with size of 3"""
vegetables = ["carrot","tomato","cucumber"]
print(vegetables)

"""3.Insert "cat" in the fruit list to the index 2"""
# fruits.insert(2,"cat")
# print(fruits)

"""4.append the fruit to vegetable list"""
# vegetables.extend(fruits)
# print(vegetables)

"""5.sort the list
•fruit list---->ascending order
•vegetable list------> descending order"""

# fruits.sort()
# print(fruits)
# vegetables.sort(reverse=True)
# print(vegetables)

"""6.Make a copy of fruit list"""
newli = fruits.copy()
print(newli)

"""7.reverse the vegetable list"""
vegetables = vegetables[::-1]
print(vegetables)
