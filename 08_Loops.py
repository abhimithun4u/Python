# Author: Abhishek Mukherjee
# Topic: Loops in Python while and for loops

i = 0
while i < 10:
    print(i)
    i = i + 1
print("While loop completed")

# For Loop to print a list
fruits = ["Banana", "Apple","Mango","Grapes","Guava","Kiwi","Orange"]
for fruit in fruits:
    print(fruit)

# For loop to print a range, range always starts from 0, but if i want to start
# a range from 1 or i will specify like range(0,5) will print 0 1 2 3 4
for j in range(0,5):
    print(j)
