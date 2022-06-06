from pickle import APPEND
from array import *
array_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Welcome to the array list")
input("Please press enter to display the array: ")
print(array_list)
print(array_list[0], array_list[1], array_list[2])
number = int(input("Please type in a Number to enter in the array: "))
array_list.append(number)
print(array_list)
array_list.reverse()
print(array_list)
print(len(array_list))