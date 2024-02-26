# Author: Abhishek Mukherjee
# Topic: Program to find the sum of n natural numbers
num = int(input("Enter The Number :-  "))
sum = 0
for i in range(1, num+1):
    sum += i
print("The Sum of ",num ,"natural numbers is", sum)