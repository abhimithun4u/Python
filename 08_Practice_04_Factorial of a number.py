# Author: Abhishek Mukherjee
# Topic: Program to find factorial of a number
num = int(input("Enter the Number:- "))
fact = 1
for i in range(1, num + 1):
    fact *= i
    i = i + 1
print("The factorial of", num, "is : ", fact)
